from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_invalid_input():

    response = client.post(
        "/predict",
        json={
            "support_calls": "abc"
        }
    )

    assert response.status_code == 422