from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd

app = FastAPI(title="ML Prediction API", description="Handles classification and regression", version="1.0")

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Load model and fit scaler on training data
try:
    model = joblib.load("models/model_classification.pkl")
    print("✅ Model loaded.")

    # Load iris data to fit scaler same way as during training
    df = pd.read_csv("data/iris.csv")
    X = df.drop("species", axis=1)
    scaler = StandardScaler()
    scaler.fit(X.select_dtypes(include=np.number))  # Fit scaler same as training
    print("✅ Scaler fitted.")
except Exception as e:
    print("❌ Error loading model or scaler:", e)
    model = None
    scaler = None

@app.get("/")
def read_root():
    return {"message": "ML Model API is running."}

@app.post("/predict")
def predict(input_data: IrisInput):
    if model is None or scaler is None:
        raise HTTPException(status_code=500, detail="Model or Scaler not loaded.")

    input_array = np.array([[
        input_data.sepal_length,
        input_data.sepal_width,
        input_data.petal_length,
        input_data.petal_width
    ]])

    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)
    return {"prediction": prediction[0]}
