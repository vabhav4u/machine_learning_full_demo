import pandas as pd
import joblib
from sklearn.metrics import classification_report

def evaluate_model():
    df = pd.read_parquet("feature_store/features.parquet")

    X = df.drop("churn", axis=1)
    y = df["churn"]

    model = joblib.load("models/model.pkl")

    predictions = model.predict(X)

    print(classification_report(y, predictions))

if __name__ == "__main__":
    evaluate_model()
