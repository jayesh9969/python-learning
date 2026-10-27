
import psycopg
from google import genai
import os
from dotenv import load_dotenv
from pgvector.psycopg import register_vector

load_dotenv()

conn = psycopg.connect(os.getenv("DATABASE_URL"))
register_vector(conn)

client = genai.Client()

query_text = "i know python basics, OOP and building REST APIs"
def match_jobs(query_text, limit=3):

    result = client.models.embed_content(model="gemini-embedding-001", contents=query_text)
    emded = result.embeddings[0].values

    query = """
    SELECT title, company_name, salary, skills, applicants_count, embedding <=> %s::vector AS distance
    FROM jobs
    ORDER BY distance ASC
    LIMIT %s

    """
    with conn.cursor() as cur:
        cur.execute(query, (emded, limit))
        rows = cur.fetchall()
        jobs = []
        for row in rows:

            job_data = {
            "title": row[0],
            "company": row[1],
            "salary": row[2],
            "skills": row[3],
            "applicants": row[4],
            "distance": round(row[5], 4),
            "competition": "Low Competition 🔥" if row[4] < 150 else "High Competition ⚡"
}
            jobs.append(job_data)

    return jobs
   

        

if __name__ == "__main__":
    print(match_jobs(query_text))

