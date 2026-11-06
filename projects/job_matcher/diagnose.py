from dotenv import load_dotenv
load_dotenv()

from langfuse import observe
from google import genai
from matcher import match_jobs

client = genai.Client()

@observe(as_type="generation")
def generate_diagnosis(candidate_profile, matched_jobs):

    prompt=f"these are the rules: {candidate_profile} this includes candidates information you have to compare with {matched_jobs} then you have to return this to user but do not write placement guaranteed, do not write that compared results matches ex. 75%. give user which role is best for them after comparing, give user which skills they are lacking from {matched_jobs}, give user shortest learning route with how much time it will take, what should user learn first."

    res = client.models.generate_content(model="gemini-3.5-flash-lite", contents=prompt)

    return res.text

if __name__ == "__main__":
    profile = "I know python basics, OOP and Building REST APIs"
    jobs = match_jobs(profile)
    print(generate_diagnosis(profile, jobs))
