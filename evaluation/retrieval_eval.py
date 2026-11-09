
import sys
import json
from pathlib import Path

# Add project root for clean imports
current_dir = Path(__file__).parent
sys.path.append(str(current_dir.parent / "projects" / "job_matcher"))
from matcher import match_jobs






def calculate_hit_rate(retrieved_jobs: list, target_keyword: str) -> float:
    """
    Returns 1.0 if target_keyword is found in any retrieved job title or skills, else 0.0.
    """

    for job in retrieved_jobs:
        if target_keyword.lower() in job["title"] or target_keyword.lower() in job["skills"]:
            return 1.0

    else:
        return 0.0
    # TODO: 1. Loop through retrieved_jobs:
    #          - check if target_keyword.lower() in job["title"].lower() or target_keyword.lower() in job["skills"].lower()
    #          - agar mil jaye, return 1.0
    # TODO: 2. Agar pura loop khatam ho jaye aur na mile, return 0.0
    pass


def calculate_reciprocal_rank(retrieved_jobs: list, target_keyword: str) -> float:
    """
    Returns 1.0 / rank of the first relevant job (1-based).
    If not found in retrieved_jobs, returns 0.0.
    """
    for rank, job in enumerate(retrieved_jobs, start=1):
        if target_keyword.lower() in job["title"] or target_keyword.lower() in job["skills"]:
            return 1.0 / rank


    return 0.0

    # TODO: 1. Loop through retrieved_jobs with 1-based index (e.g. enumerate(retrieved_jobs, start=1)):
    #          - agar match mile rank 'rank' par, return 1.0 / rank
    # TODO: 2. Agar match na mile, return 0.0
    pass


def run_retrieval_benchmark():
    test_cases = [
        {
            "query": "Junior Python Developer knowing OOP and Git",
            "target": "Python"
        },
        {
            "query": "Data Analyst Trainee skilled in SQL and Excel",
            "target": "Data"
        },
        {
            "query": "Junior Full Stack Developer with React and HTML",
            "target": "Developer"
        }
    ]

    print(f"🔍 Evaluating Supabase Vector Retrieval on {len(test_cases)} queries...\n")

    hits = []
    rrs = []

    for tc in test_cases:
        jobs = match_jobs(tc["query"], limit=3)
        
        hit = calculate_hit_rate(jobs, tc["target"])
        rr = calculate_reciprocal_rank(jobs, tc["target"])

        hits.append(hit)
        rrs.append(rr)

        top_titles = [j["title"] for j in jobs]
        print(f"Query: '{tc['query'][:35]}...'")
        print(f"  Top 3 Titles: {top_titles}")
        print(f"  Hit: {hit} | Reciprocal Rank: {round(rr, 2)}\n")

    mean_hit_rate = sum(hits) / len(hits)
    mrr = sum(rrs) / len(rrs)

    print("========================================")
    print("RETRIEVAL EVALUATION REPORT")
    print("========================================")
    print(f"Mean Hit Rate (Recall@3): {round(mean_hit_rate * 100, 1)}%")
    print(f"Mean Reciprocal Rank (MRR): {round(mrr, 3)}")
    print("========================================")


if __name__ == "__main__":
    run_retrieval_benchmark()

