import json
import joblib
import pandas as pd

# Load artifacts once when API starts
model = joblib.load("artifacts/model.pkl")

with open("artifacts/feature_columns.json", "r") as f:
    feature_columns = json.load(f)


def prepare_features(data: dict):

    df = pd.DataFrame([{
        "Support Calls": data["support_calls"],
        "Total Spend": data["total_spend"],
        "Payment Delay": data["payment_delay"],
        "Last Interaction": data["last_interaction"],
        "Subscription Type": data["subscription_type"],
        "Contract Length": data["contract_length"]
    }])

    # Same transformation used during training
    df = pd.get_dummies(df, drop_first=True)

    # Add missing columns
    for col in feature_columns:
        if col not in df.columns:
            df[col] = 0

    # Keep exact training order
    df = df[feature_columns]

    return df


def predict_churn(data: dict):

    X = prepare_features(data)

    prediction = model.predict(X)[0]

    probability = model.predict_proba(X)[0][1]

    return {
        "prediction": int(prediction),
        "churn_probability": round(float(probability), 4)
    }