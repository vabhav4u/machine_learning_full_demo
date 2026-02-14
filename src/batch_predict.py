import pandas as pd
import mlflow.pyfunc

mlflow.set_tracking_uri("file:./mlruns")

model = mlflow.pyfunc.load_model(
    model_uri="models:/ChurnModel/Production"
)

df = pd.read_csv("predict/input.csv")

# Feature engineering same as training
df["spend_per_tenure"] = df["monthly_spend"] / (df["tenure"] + 1)
df = pd.get_dummies(df, columns=["contract_type"], drop_first=True)

prediction = model.predict(df)

print("Prediction Result:", prediction)
