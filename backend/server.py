from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pickle
import pandas as pd
import os
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging

# Initialize the FastAPI app
app = FastAPI()

# Define the paths to the model file and label encoder
model_path = 'C:\\Users\\user\\Desktop\\Crop Recommendation\\XGBoost.pkl'
label_encoder_path = 'C:\\Users\\user\\Desktop\\Crop Recommendation\\label_encoder.pkl'

# List of crop labels (as shared)
crop_labels = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
               'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
               'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
               'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Load the specified model and label encoder
def load_model():
    if not os.path.exists(model_path):
        raise FileNotFoundError("The specified model file does not exist.")
    
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    
    return model

def load_label_encoder():
    if not os.path.exists(label_encoder_path):
        raise FileNotFoundError("The specified label encoder file does not exist.")
    with open(label_encoder_path, 'rb') as file:
        le = pickle.load(file)
    
    return le

# Load the model and label encoder at the start
try:
    model = load_model()
    label_encoder = load_label_encoder()
    logging.info("Model and label encoder loaded successfully.")
except Exception as e:
    logging.error(f"Failed to load model or label encoder: {str(e)}")
    raise RuntimeError(f"Failed to load model or label encoder: {str(e)}")

# Define the input data structure with validation constraints
class CropData(BaseModel):
    N: float = Field(..., ge=0, le=150, description="Nitrogen (N) must be between 0 and 150.")
    P: float = Field(..., ge=0, le=150, description="Phosphorus (P) must be between 0 and 150.")
    K: float = Field(..., ge=0, le=220, description="Potassium (K) must be between 0 and 220.")
    temperature: float = Field(..., ge=0, le=50, description="Temperature must be between 0 and 50°C.")
    humidity: float = Field(..., ge=0, le=100, description="Humidity must be between 0 and 100%.")
    ph: float = Field(..., ge=0, le=10, description="pH must be between 0 and 10.")
    rainfall: float = Field(..., ge=0, le=300, description="Rainfall must be between 0 and 300 mm.")

# Enable CORS
orig_main = ["http://localhost:3000"]  # URL of your React app
app.add_middleware(
    CORSMiddleware,
    allow_origins=orig_main,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Crop Recommendation System API is running."}

# Predict endpoint
@app.post("/predict/")
def predict(data: CropData):
    try:
        # Log incoming request data
        logging.info(f"Received data: {data.dict()}")
        
        # Prepare data for prediction
        input_data = pd.DataFrame([data.dict()])
        
        # Make prediction and get probability
        probabilities = model.predict_proba(input_data)[0]  # Probabilities for each class
        prediction_index = model.predict(input_data)[0]
        prediction_index = int(prediction_index)
        
        # Map prediction index to crop label
        if 0 <= prediction_index < len(crop_labels):
            predicted_crop = crop_labels[prediction_index]
            probability = probabilities[prediction_index] * 100  # Convert to percentage
        else:
            raise ValueError("Prediction index is out of range.")
        
        return {
            "prediction": predicted_crop,
            "probability": round(probability, 2)  # Round to 2 decimal places
        }

    except ValueError as ve:
        logging.error(f"ValueError: {str(ve)}")
        return JSONResponse(
            status_code=400,
            content={"error": "Invalid input data", "message": str(ve)}
        )
    except FileNotFoundError as fnfe:
        logging.error(f"FileNotFoundError: {str(fnfe)}")
        return JSONResponse(
            status_code=500,
            content={"error": "File not found", "message": str(fnfe)}
        )
    except Exception as e:
        logging.error(f"Exception: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": "Server error", "message": "An unexpected error occurred."}
        )

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
