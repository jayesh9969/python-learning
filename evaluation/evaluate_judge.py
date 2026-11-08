from dotenv import load_dotenv
load_dotenv()

import json
from google import genai
from google.genai import types
from pydantic import BaseModel

class EvaluationResult(BaseModel):
    score: float  # 1.0 = Fully grounded/faithful, 0.0 = Hallucinated / unsupported
    reason: str

client = genai.Client()

def evaluate_faithfulness(candidate_profile: str, retrieved_jobs: list, diagnosis: str) -> EvaluationResult:
    """
    LLM-as-a-Judge: Checks whether the diagnosis is strictly grounded in retrieved_jobs.
    """

    judge_prompt = f"You are an expert AI quality evaluator, Context({retrieved_jobs}),{candidate_profile},{diagnosis} Rules: if there is skill or claim in the {diagnosis} which is not present in {retrieved_jobs} then give a score 0.0 . if all claims are grounded then give a score 1.0 ."

    res = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=judge_prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=EvaluationResult
        )
    
    )
    return res.parsed
    # TODO: 1. Judge prompt taiyar kijiye jisme:
    #       - Judge ko uski role batao ("You are an expert AI quality evaluator...")
    #       - Context (retrieved_jobs), candidate_profile, aur diagnosis provide karo
    #       - Rule do: Agar diagnosis me koi aisa skill ya claim hai jo retrieved_jobs me nahi hai, toh score 0.0 do. Agar saare claims grounded hain, toh score 1.0 do.
    
    # TODO: 2. Gemini 3.5 Flash-Lite ko call kijiye with types.GenerateContentConfig(
    #           response_mime_type="application/json",
    #           response_schema=EvaluationResult
    #          )

    # TODO: 3. Return parsed EvaluationResult
    pass


if __name__ == "__main__":
    sample_jobs = [
        {
            "title": "Junior Python Developer",
            "skills": "Python, OOP, SQL, Git",
            "company": "TechCorp"
        }
    ]
    candidate = "I know Python basics and Git."

    # Test Case 1: Faithful (Grounded in context)
    good_diagnosis = "Your profile matches Python and Git. To qualify, you should learn OOP and SQL next."
    print("--- Testing Faithful Diagnosis ---")
    result1 = evaluate_faithfulness(candidate, sample_jobs, good_diagnosis)
    print(f"Score: {result1.score}")
    print(f"Reason: {result1.reason}\n")

    # Test Case 2: Hallucinated (Invented skills not in jobs)
    bad_diagnosis = "You must master Kubernetes, Docker, Rust, and AWS cloud architecture immediately."
    print("--- Testing Hallucinated Diagnosis ---")
    result2 = evaluate_faithfulness(candidate, sample_jobs, bad_diagnosis)
    print(f"Score: {result2.score}")
    print(f"Reason: {result2.reason}")

