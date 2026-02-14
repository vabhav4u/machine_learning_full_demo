import pandas as pd
import os
import json
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model():
    df = pd.read_parquet("feature_store/features.parquet")

    X = df.drop("churn", axis=1)
    y = df["churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Using RandomForestClassifier....")
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/model.pkl")

    with open("models/metrics.json", "w") as f:
        json.dump({"accuracy": acc}, f)

    print(f"Model trained. Accuracy: {acc:.4f}")

if __name__ == "__main__":
    train_model()
