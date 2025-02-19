# tests/test_summarizer.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_summarize_meeting():
    # A simple transcript for testing purposes.
    transcript = (
        "In today's meeting, we discussed the upcoming product launch. "
        "Jane will follow up with the design team, and John is tasked with finalizing the marketing strategy. "
        "We agreed to reconvene next week."
    )
    payload = {"transcript": transcript}
    response = client.post("/summarize/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
    # Optionally, check that the output contains keywords like "Summary:" and "Action Items:"
    assert "Summary:" in data["result"]
    assert "Action Items:" in data["result"]
