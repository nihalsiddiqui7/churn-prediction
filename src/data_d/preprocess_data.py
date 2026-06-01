import pandas as pd


def preprocess_data(df: pd.DataFrame, target_column: str) -> pd.DataFrame:
    """"
    Preprocess the dataset by :
    1- Trimming whitespace from string columns.
    2- Dropping missing values.
    3- mapping target labels to binary values (0 and 1) if not already done.
    4- Dropping ID column
    """

    # Trim whitespace from string columns
    df.columns = df.columns.str.strip()

    # Drop missing values
    df = df.dropna()

    # Map target labels to binary values if not already done
    if df[target_column].dtype == 'object':
        df[target_column] = df[target_column].map({'Yes': 1, 'No': 0})

    # Drop ID column if it exists
    for col in ['CustomerID', 'customerID']:
        if col in df.columns:
            df = df.drop(columns=[col])
            break

    return df