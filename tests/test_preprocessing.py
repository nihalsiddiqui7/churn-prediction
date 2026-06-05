import pandas as pd

from src.data_d.preprocess_data import preprocess_data

def test_preprocessing():

    df = pd.read_csv(
        "data/raw/customer_churn_dataset.csv"
    )

    result = preprocess_data(
        df,
        "Churn"
    )

    assert result is not None