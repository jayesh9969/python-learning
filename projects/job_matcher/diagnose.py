from google import genai

from dotenv import load_dotenv

from matcher import match_jobs

load_dotenv()

profile = "I know python basics, OOP and Building REST APIs"

jobs = match_jobs(profile)

client = genai.Client()
def generate_diagnosis(candidate_profile, matched_jobs):

    prompt=f"these are the rules: {candidate_profile} this includes candidates information you have to compare with {matched_jobs} then you have to return this to user but do not write placement guaranteed, do not write that compared results matches ex. 75%. give user which role is best for them after comparing, give user which skills they are lacking from {matched_jobs}, give user shortest learning route with how much time it will take, what should user learn first."

    res = client.models.generate_content(model="gemini-flash-lite-latest", contents=prompt)

    return res.text

if __name__ == "__main__":
    print(generate_diagnosis(profile, jobs))
