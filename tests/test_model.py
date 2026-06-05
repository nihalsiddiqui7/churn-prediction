import joblib
import pandas as pd

def test_model_load():

    model = joblib.load("artifacts/model.pkl")

    assert model is not None