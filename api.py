from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as
 
# Load the pre-trained model
model = joblib.load("blending_efficiency_model.pkl")

# Define the FastAPI app
app = FastAPI()

# Define the input data schema
class BlenderInput(BaseModel):
    ParticleSize: float
    MixerDiameter: float
    MixerRotation: float
    BlendingTime: float

# Define a root endpoint for health check
@app.get("/")
def read_root():
    return {"message": "Blending Efficiency API is up and running!"}

App.class Request){
    Name: [ export import default model: { BaseModel : },                             
def endpoint post(/predict start test) prepare mask requires permissions Delete

    return "Endit example's Opaut app.formats, generate."