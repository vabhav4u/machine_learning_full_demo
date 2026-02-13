import pandas as pd
import os

def clean_data():
    df = pd.read_csv("../data/raw/customers.csv")
    
    print("Dropping Duplicates .......")
    df = df.drop_duplicates()
    print("Dropping NAs.......")
    df = df.dropna()

    os.makedirs("../data/processed", exist_ok=True)
    df.to_csv("../data/processed/cleaned.csv", index=False)

    print("Cleaned data saved to ../data/processed/cleaned.csv")

if __name__ == "__main__":
    clean_data()
