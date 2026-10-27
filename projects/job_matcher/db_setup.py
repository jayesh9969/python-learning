from google import genai
import os
import psycopg
from pgvector.psycopg import register_vector
from dotenv import load_dotenv

load_dotenv()

conn = psycopg.connect(os.getenv("DATABASE_URL"))

with conn.cursor() as cur:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
        id SERIAL PRIMARY KEY,
        title TEXT,
        company_name TEXT,
        salary TEXT,
        experience TEXT,
        skills TEXT,
        location_type TEXT, -- 'remote','hybrid','onsite',
        company_type TEXT, -- 'startup','mid','mnc',
        recruiter_reputation TEXT, -- 'verified','standard',
        applicants_count INT,
        apply_url TEXT,
        description TEXT,
        embedding VECTOR(3072)
        );
    """)
conn.commit() 

print("Job table created successfully!")

conn.close()