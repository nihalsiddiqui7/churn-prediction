# test_pipeline_phase1.py
import os
import pandas as pd

# Make sure Python can find your src package
import sys
sys.path.append(os.path.abspath("src"))

from data_d.load_data import load_data
from data_d.preprocess_data import preprocess_data
from features.build_features import feature_engineering
from utils.validate import validate_data

# === CONFIG ===
DATA_PATH = "D:\\Data science\\Portfolio Projects\\churn_prediction\\churn-prediction\\data\\raw\\customer_churn_dataset.csv"  # adjust to your file path
TARGET_COL = "Churn"

def main():
    print("=== Testing Phase 1: Load → Preprocess → Build Features ===")

    # 1. Load Data
    print("\n[1] Loading data...")
    df = load_data(DATA_PATH)
    print(f"Data loaded. Shape: {df.shape}")
    print(df.head(3))

    #validate data 
    print("\nValidating data...")
    validate_data(df)
    print("Data validation passed!")
    
    # 2. Preprocess
    print("\n[2] Preprocessing data...")
    df_clean = preprocess_data(df, target_column='Churn')
    print(f"Data after preprocessing. Shape: {df_clean.shape}")
    print(df_clean.head(3))

    # 3. Build Features
    print("\n[3] Building features...")
    df_features = feature_engineering(df_clean)
    print(f"Data after feature engineering. Shape: {df_features.shape}")
    print(df_features.head(3))

    print("\n✅ Phase 1 pipeline completed successfully!")

if __name__ == "__main__":
    main()