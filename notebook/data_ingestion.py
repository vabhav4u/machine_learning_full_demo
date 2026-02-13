import pandas as pd
import numpy as np
import os
from sklearn.datasets import make_classification

def generate_data():
    X, y = make_classification(
        n_samples=1500,
        n_features=5,
        n_informative=4,
        n_redundant=0,
        random_state=42
    )
    df = pd.DataFrame(X, columns=[
        "age", "tenure", "monthly_spend",
        "support_calls", "usage_score"
    ])

    df["age"] = (df["age"] * 10 + 40).abs().astype(int)
    df["tenure"] = (df["tenure"] * 5 + 12).abs().astype(int)
    df["monthly_spend"] = (df["monthly_spend"] * 2000 + 5000).abs()
    df["support_calls"] = (df["support_calls"] * 2 + 3).abs().astype(int)

    df["contract_type"] = np.random.choice(
        ["monthly", "yearly", "two_year"],
        size=len(df)
    )

    df["churn"] = y

    os.makedirs("../data/raw", exist_ok=True)
    df.to_csv("../data/raw/customers.csv", index=False)
    print("Raw data saved to ../data/raw/customers.csv")

if __name__ == "__main__":
    generate_data()
