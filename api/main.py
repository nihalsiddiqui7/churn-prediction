from fastapi import FastAPI

from api.schemas import CustomerData
from api.predictor import predict_churn

app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Customer Churn API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict(customer: CustomerData):

    result = predict_churn(customer.model_dump())

    return result