from dotenv import load_dotenv
load_dotenv()

from langfuse import observe
from fastapi import FastAPI
from pydantic import BaseModel

from matcher import match_jobs
from diagnose import generate_diagnosis

app = FastAPI()

class CandidateRequest(BaseModel):
    profile:str


@app.get("/")
def health_check():

    return {"status": "running", "service": "Job Matcher API"}


@app.post("/analyze")
@observe()
def analyze_response(body : CandidateRequest):

    jobs = match_jobs(body.profile)
    report = generate_diagnosis(body.profile, jobs)

    return {"matched_jobs": jobs, "diagnosis": report}


