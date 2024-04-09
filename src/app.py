# Imports
from typing import Union
from fastapi import FastAPI, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse  # Import FileResponse
import pickle
from pydantic import BaseModel
import pandas as pd
import os
import uvicorn
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Setup Section
# Creating FastAPI instance
app = FastAPI(title="Sepsis Predictor: The Sepsis API", description="API for Sepsis Prediction")

# Mounting static files directory
app.mount("/static", StaticFiles(directory="src/static"), name="static")

## A function to load machine learning components for reuse
def load_ml_components(filepath):
    with open(filepath, "rb") as file:
        loaded_object = pickle.load(file)
        return loaded_object

# Define the directory path
directory_path = os.getcwd()

# Loading machine learning components
ml_model_filename = "ML_Model.pkl"
ml_model_filepath = os.path.join(directory_path, "src", "models", ml_model_filename)
ml_components_dict = load_ml_components(filepath=ml_model_filepath)

# Defining variables for each component
label_encoder = ml_components_dict['label_encoder']  # Label encoder
scaler = ml_components_dict['scaler']  # Loaded scaler
model = ml_components_dict['model']  # Loaded model

# Defining input variables
class InputData(BaseModel):
    PRG: int
    PL: int
    BP: int
    SK: int
    TS: int
    BMI: float
    BD2: float
    Age: int

"""
* PRG: Plasma glucose
* PL: Blood Work Result-1 (mu U/ml)
* BP: Blood Pressure (mmHg)
* SK: Blood Work Result-2 (mm)
* TS: Blood Work Result-3 (muU/ml)
* BMI: Body mass index (weight in kg/(height in m)^2)
* BD2: Blood Work Result-4 (mu U/ml)
* Age: patient's age (years)
"""

# Index route
@app.get("/")
async def index():
    return FileResponse(os.path.join("src", "templates", "index.html"))  # Adjust filepath

# Prediction endpoint
@app.post("/predict")
def predict(df: InputData):
    # Prepare features and structure them
    df = pd.DataFrame([df.dict().values()], columns=df.dict().keys())

    print(f"[Info] Input dataframe: {df.to_markdown()}")
    age = df['Age']
    print(age)

    # Scaling the inputs
    df_scaled = scaler.transform(df)

    # Make prediction
    raw_predictions = model.predict(df_scaled)

    if 1 in raw_predictions:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="The patient is predicted to develop Sepsis")
    else:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="The patient is not predicted to develop Sepsis")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=7860, reload=True)  # Adjust module name