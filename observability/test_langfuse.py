from dotenv import load_dotenv

from langfuse import observe, Langfuse

load_dotenv()

langfuse = Langfuse()

@observe()
def search_jobs(profile: str):
    return [{"title": "Junior AI Engineer", "similarity": 0.88}]

@observe(as_type="generation")

def ai_dignosis(jobs: list, profile: str):
    return "Shortest route: Learn FastAPI and Supabase to match Junior AI Engineer."
    


@observe()
def run_pipeline(profile: str):
    jobs = search_jobs(profile)
    diagnosis = ai_dignosis(jobs, profile)
    

    return diagnosis

if __name__ == "__main__":

    result = run_pipeline("Python beginner seeking AI role")

    langfuse.flush()

    print("pipeline diagnosis:", result)



