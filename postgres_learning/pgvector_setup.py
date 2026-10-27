from google import genai
import os
import psycopg
from pgvector.psycopg import register_vector
from dotenv import load_dotenv

load_dotenv()

conn = psycopg.connect(os.getenv("DATABASE_URL"))
register_vector(conn)

with conn.cursor() as cur:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS food_items (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            price NUMERIC,
            is_veg BOOLEAN,
            embedding VECTOR(3072)
        );
    """)
conn.commit()
items = [
    ("Paneer Butter Masala", 180, True),
    ("Butter Chicken", 250, False),
    ("Dal Tadka", 120, True),
    ("Chicken Biryani", 220, False),
]


with conn.cursor() as cur:

    for name, price, is_veg in items:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        res = client.models.embed_content(model="gemini-embedding-001", contents=name)
        emb = res.embeddings[0].values
        cur.execute(
        """
        INSERT INTO food_items (name, price, 
        is_veg, embedding)
        VALUES (%s, %s, %s, %s);
        """,
        (name, price, is_veg, emb)
    
           
    )

conn.commit()

search_text = "cottage cheese in red gravy"
res2 = client.models.embed_content(model="gemini-embedding-001", contents=search_text)
emb2 = res2.embeddings[0].values

query = """
    SELECT name, price, is_veg, embedding <=> %s ::vector AS distance
    FROM food_items
    WHERE is_veg = %s AND price < %s
    ORDER BY distance ASC
    LIMIT 1;

"""

with conn.cursor() as cur:
    cur.execute(query, (emb2, True, 200))

    results = cur.fetchall()

    for row in results:
        print(f"Name: {row[0]}, Price: {row[1]}, Distance: {row[3]:.4f}")

conn.close()








