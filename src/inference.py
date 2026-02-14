import argparse
import pandas as pd
import joblib

def predict(args):
    model = joblib.load("models/model.pkl")

    input_data = pd.DataFrame([{
        "age": args.age,
        "tenure": args.tenure,
        "monthly_spend": args.monthly_spend,
        "support_calls": args.support_calls,
        "usage_score": args.usage_score,
        "spend_per_tenure": args.monthly_spend / (args.tenure + 1),
        "contract_type_two_year": 1 if args.contract_type == "two_year" else 0,
        "contract_type_yearly": 1 if args.contract_type == "yearly" else 0
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    print(f"Churn Probability: {probability:.4f}")
    print("Prediction:", "Likely to Churn" if prediction == 1 else "Not Likely")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--age", type=float, required=True)
    parser.add_argument("--tenure", type=float, required=True)
    parser.add_argument("--monthly_spend", type=float, required=True)
    parser.add_argument("--support_calls", type=float, required=True)
    parser.add_argument("--usage_score", type=float, required=True)
    parser.add_argument("--contract_type", type=str, required=True)

    args = parser.parse_args()
    predict(args)
