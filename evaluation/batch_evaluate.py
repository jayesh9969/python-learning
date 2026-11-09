import sys
import json
from pathlib import Path

# Add project roots for clean imports
current_dir = Path(__file__).parent
sys.path.append(str(current_dir.parent / "projects" / "job_matcher"))
sys.path.append(str(current_dir))

from matcher import match_jobs
from diagnose import generate_diagnosis
from evaluate_judge import evaluate_faithfulness


def run_benchmark(dataset_path: str = "evaluation/test_dataset.json"):
    """
    Runs automated batch evaluation over the test dataset and prints an aggregate quality report.
    """
    # 1. Load dataset from JSON
    with open(dataset_path, "r", encoding="utf-8") as f:
        test_cases = json.load(f)

    print(f"🚀 Running AI Benchmark on {len(test_cases)} test cases...\n")

    scores = []

    for tc in test_cases:
        
        jobs = match_jobs(tc["profile"])


        diagnosis = generate_diagnosis(tc["profile"], jobs)

        result = evaluate_faithfulness(tc["profile"], jobs, diagnosis)
        scores.append(result.score)

    avg_score = sum(scores) / len(scores)
    print("BENCHMARK SUMMARY REPORT")

    if avg_score >= 0.8:
        print(f"Total Cases Tested: {len(test_cases)}")
        print(f"Average Faithfullness: {avg_score}")
        print("Status: BENCHMARK PASSED")

    else:
        print("BENCHMARK FAILED")

    # TODO: 2. Har test case par loop chalaiye:
    #       - profile = tc["profile"]
    #       - jobs = match_jobs(profile)
    #       - diagnosis = generate_diagnosis(profile, jobs)
    #       - eval_result = evaluate_faithfulness(profile, jobs, diagnosis)
    #       - scores list me eval_result.score add kijiye
    #       - Terminal par print kijiye: Test Case ID, Domain, aur Score

    # TODO: 3. Calculate average faithfulness score:
    #       avg_score = sum(scores) / len(scores)

    # TODO: 4. Print benchmark summary:
    #       - Total tests run
    #       - Average Faithfulness Score (percentage)
    #       - Pass threshold: Agar avg_score >= 0.8 toh "BENCHMARK PASSED ✅", warna "BENCHMARK FAILED ❌"

    return avg_score  # replace with avg_score


if __name__ == "__main__":
    run_benchmark()

