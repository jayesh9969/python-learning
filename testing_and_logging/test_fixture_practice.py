
import pytest

@pytest.fixture

def sample_candidate():

    return {"name": "jayu", "skills": ["Python", "SQL"], "experience": 2}


def test_candidate_skills(sample_candidate):
    assert len(sample_candidate["skills"]) == 2
    sample_candidate["skills"].append("FastAPI")

    assert len(sample_candidate["skills"]) == 3
    sample_candidate["skills"].append("FastAPI")
        
        
def test_fresh_candidate(sample_candidate):

    assert len(sample_candidate["skills"]) == 2
    sample_candidate["skills"].append("FastAPI")



