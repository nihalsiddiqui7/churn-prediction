import pandas as pd


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform Feature Engineering Steps like
    1-One-Hot Encoding for categorical features.
    2-Feature Scaling is not needed for tree-based models but can be added if necessary.(we will skip it for now)
    """

    # One-Hot Encoding for categorical features
    categorical_cols = df.select_dtypes(include=['object']).columns
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    return df