from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_predict():

    response = client.post(
        "/predict",
        json={
            "support_calls": 5,
            "total_spend": 1000,
            "payment_delay": 5,
            "last_interaction": 10,
            "subscription_type": "Premium",
            "contract_length": "Annual"
        }
    )

    assert response.status_code == 200