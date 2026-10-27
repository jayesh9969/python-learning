import psycopg
from google import genai
from dotenv import load_dotenv
from pgvector.psycopg import register_vector
import os


load_dotenv()

conn = psycopg.connect(os.getenv("DATABASE_URL"))


register_vector(conn)

client = genai.Client()

job_list = [
    ("Ai Ml Intern", "zoom", "5lac per annum", "0 - 1 years", "scikit, pytorch and machine leaerning basics", "remote", "mid", "verified", 100, "wellfound.com", "Looking for an AI/ML intern to build agentic workflows and evaluate LLM outputs"),
    ("Junior Python Developer", "GitDrop", "7lac per annum", "0 - 2 years", "OOP, data structures, error handling, functions, python basics", "onsite","startup","verified", 200, "gitdrop.com", "Looking for python developer who can write and fix code also who can build or connect REST APIs"),
    ("Web Developer", "akashi", "3 - 5lac per annum", "2 years", "HTML5, CSS3, JS, API dev,Databases","hybrid", "startup", "verified", 250, "ycombinator.com", "Looking for an web developer who can write and edit code and assist senior engineers"),
    ("Junior Full Stack Developer", "OrBiz", "9lac per annum", "3 - 5 years", "html,css,js,React,angular,java, api and protocols","hybrid","startup", "verified", 200, "ycombinator.com", "Looking for an jr. full stack developer who can write and fix code, able to handle front end and backend tasks"),
    ("Data Analyst Trainee", "datadump", "4 - 6lac per annum", "0 - 1 years", "SQL, Excel,tablau, stats and probability, python or R", "remote","mid", "verified", 220, "wellfound.com", "Looking for an data analyst trainee who can run basic queries,gather raw data from databases and build charts and graphs"),
    ("Junior QA Test Engineer", "sansuk", "4 - 6lac per annum", "0 - 2 years", "testing fundamentals, manual testing types, basic API testing, selenium basics, defects and project managements", "onsite", "startup", "verified", 80, "ycombinator.com", "Looking for an jr. qa test engineer who can execute test cases,find bugs and perform regression testing")
]

with conn.cursor() as cur:
    for title,company_name, salary,experience, skills, location_type,company_type, recruiter_reputation,applicants_count, apply_url,description in job_list:
        res = client.models.embed_content(model="gemini-embedding-001", contents=description)
        emb = res.embeddings[0].values
        cur.execute(
         """
        INSERT INTO jobs (title,company_name, salary,experience, skills, location_type,company_type, recruiter_reputation,applicants_count, apply_url,description,embedding)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
        """,
        (title,company_name, salary,experience, skills, location_type,company_type, recruiter_reputation,applicants_count, apply_url,description, emb)
    )
conn.commit()

print("All 6 jobs seeded successfully")

conn.close()

