from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

# Create the FastAPI app
app = FastAPI()

# Define the input schema
class IrisRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Load the model
model_path = os.path.join(os.path.dirname(__file__), "../model/model.pkl")
model = joblib.load(model_path)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris prediction API!"}

@app.post("/predict")
def predict_species(data: IrisRequest):
    features = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}
