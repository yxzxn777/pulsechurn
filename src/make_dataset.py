import pandas as pd
from pathlib import Path

# Paths
RAW_PATH = Path("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")
PROCESSED_PATH = Path("data/processed/churn_clean.csv")

def load_raw_data():
    df = pd.read_csv(RAW_PATH)
    print(f"Loaded raw data: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

def clean_data(df):
    # Fix TotalCharges — it's loaded as string, has spaces for new customers
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Drop the customerID column — not useful for modeling
    df = df.drop(columns=["customerID"])

    # Convert target to binary integer
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    print(f"Missing values after cleaning:\n{df.isnull().sum()[df.isnull().sum() > 0]}")
    print(f"Churn distribution:\n{df['Churn'].value_counts()}")

    return df

def save_processed(df):
    df.to_csv(PROCESSED_PATH, index=False)
    print(f"Saved cleaned data to {PROCESSED_PATH}")

if __name__ == "__main__":
    df = load_raw_data()
    df = clean_data(df)
    save_processed(df)