import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    res = client.get("/")

    assert res.json()["status"] == "running"


def test_analyze_endpoint():
    res = client.post("/analyze", json={"profile": "Python developer with OOP and REST API skills"})

    assert res.status_code == 200

    data = res.json()


    assert "matched_jobs" in data

    assert "diagnosis" in data

    len(data["matched_jobs"]) > 0