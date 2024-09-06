
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize FastAPI app
app = FastAPI()

# Load the pre-trained model
model = joblib.load("model.pkl")

# Define the request body structure
class PredictRequest(BaseModel):
    as90: float
    g33: float
    mak: float

# Define the prediction endpoint
@app.post("/predict/")
def predict(data: PredictRequest):
    # Prepare data for prediction
    input_data = np.array([[data.as90, data.g33, data.mak]])
    
    # Make the prediction
    prediction = model.predict(input_data)
    
    return {"predicted_ift": prediction[0]}
