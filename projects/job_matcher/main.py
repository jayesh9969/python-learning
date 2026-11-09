from dotenv import load_dotenv
load_dotenv()

from langfuse import observe
from fastapi import FastAPI
from pydantic import BaseModel

from matcher import match_jobs
from diagnose import generate_diagnosis
from guardrails import secure_user_input
from fastapi import FastAPI, HTTPException

app = FastAPI()

class CandidateRequest(BaseModel):
    profile:str


@app.get("/")
def health_check():

    return {"status": "running", "service": "Job Matcher API"}


@app.post("/analyze")
@observe()
def analyze_response(body : CandidateRequest):

    

    sec = secure_user_input(body.profile)

    if not sec["allowed"]:
        raise HTTPException(status_code=400, detail=sec["reason"])

    safe_profile = sec["sanitized_text"]
    jobs = match_jobs(safe_profile)
    report = generate_diagnosis(safe_profile, jobs)

    return {"matched_jobs": jobs, "diagnosis": report}


