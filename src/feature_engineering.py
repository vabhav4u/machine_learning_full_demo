import pandas as pd
import os
from sklearn.preprocessing import StandardScaler

def engineer_features():
    df = pd.read_csv("data/processed/cleaned.csv")
    print("Adding spend_per_tenure ...  ")    
    df["spend_per_tenure"] = df["monthly_spend"] / (df["tenure"] + 1)

    print("One-Hot Encoding on a categorical column named contract_type  ...  ")
    df = pd.get_dummies(df, columns=["contract_type"], drop_first=True)

    scaler = StandardScaler()
    numeric_cols = ["age", "tenure", "monthly_spend",
                    "support_calls", "usage_score",
                    "spend_per_tenure"]
    print("Scaling numeric values >0..<1")
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    os.makedirs("feature_store", exist_ok=True)
    df.to_parquet("feature_store/features.parquet", index=False)

    print("Feature store saved to feature_store/features.parquet")
    print(df.columns)

if __name__ == "__main__":
    engineer_features()
