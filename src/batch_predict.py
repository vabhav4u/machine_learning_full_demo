import pandas as pd
import joblib
import os

def main():

    # Load trained model
    model_path = "models/model.pkl"

    if not os.path.exists(model_path):
        raise FileNotFoundError("Model file not found in models/model.pkl")

    model = joblib.load(model_path)

    # Load prediction input CSV
    input_path = "predict/input.csv"

    if not os.path.exists(input_path):
        raise FileNotFoundError("Input CSV not found in predict/input.csv")

    df = pd.read_csv(input_path)

    print("Input Data:")
    print(df)

    # Feature engineering (must match training)
    df["spend_per_tenure"] = df["monthly_spend"] / (df["tenure"] + 1)

    # One-hot encoding (match training structure)
    df = pd.get_dummies(df, columns=["contract_type"], drop_first=True)

    # Ensure required dummy columns exist
    for col in ["contract_type_yearly", "contract_type_two_year"]:
        if col not in df.columns:
            df[col] = 0

    # Arrange columns in correct order (important!)
    expected_columns = [
        "age",
        "tenure",
        "monthly_spend",
        "support_calls",
        "usage_score",
        "spend_per_tenure",
        "contract_type_two_year",
        "contract_type_yearly"
    ]

    df = df[expected_columns]

    # Make prediction
    prediction = model.predict(df)

    df["prediction"] = prediction

    print("\nPrediction Result:")
    print(df[["prediction"]])

    # Save output
    os.makedirs("predict/output", exist_ok=True)
    output_path = "predict/output/predictions.csv"
    df.to_csv(output_path, index=False)

    print(f"\nPredictions saved to {output_path}")


if __name__ == "__main__":
    main()
