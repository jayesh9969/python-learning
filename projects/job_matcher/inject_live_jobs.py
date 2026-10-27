import requests
import psycopg
import os
from pgvector.psycopg import register_vector
from dotenv import load_dotenv
from google import genai

load_dotenv()

conn = psycopg.connect(os.getenv("DATABASE_URL"))

register_vector(conn)

url = "https://remotive.com/api/remote-jobs?category=software-dev&limit=5"

res = requests.get(url)

data = res.json()

client = genai.Client()

for job in data["jobs"][: 10]:

    title = job["title"]
    company_name = job["company_name"]
    salary = job.get("salary") or "Competitive / Disclosed on interview"
    experience = "0 - 2 years"
    skills = "".join(job.get("tags", []))
    location_type = "remote"
    company_type = "startup"
    recruiter_reputation = "verified"
    applicants_count = 65

    apply_url = job.get("url", "")
    description = job.get("description", ", ")[: 1000]

    result = client.models.embed_content(model="gemini-embedding-001", contents=description)
    emb = result.embeddings[0].values
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO jobs (title,company_name, salary,experience, skills, location_type,company_type, recruiter_reputation,applicants_count, apply_url,description,embedding)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
            """,
            (title,company_name, salary,experience, skills, location_type,company_type, recruiter_reputation,applicants_count, apply_url,description, emb)
        )
    

conn.commit()

conn.close()

print("Live jobs ingested successfully")
