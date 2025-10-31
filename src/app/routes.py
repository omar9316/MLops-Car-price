# src/app/routes.py
from fastapi import APIRouter
from src.app.schemas import PredictionRequest
import joblib
import os

router = APIRouter()

# Chemin vers le modèle
MODEL_PATH = os.path.join(os.getcwd(), "models", "rf_model.joblib")

# Charger le modèle à l'initialisation
rf_model = joblib.load(MODEL_PATH)

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/predict")
def predict_price(request: PredictionRequest):
    """
    Endpoint de prédiction réel
    """
    # Transformer les données en DataFrame
    input_df = {
        "company": [request.brand],
        "year": [request.year],
        "owner": [request.owner],
        "fuel": [request.fuel],
        "seller_type": [request.seller_type],
        "transmission": [request.transmission],
        "km_driven": [request.km_driven],
        "mileage_mpg": [request.mileage_mpg],
        "engine_cc": [request.engine_cc],
        "max_power_bhp": [request.max_power_bhp],
        "torque_nm": [request.torque_nm],
        "seats": [request.seats]
    }

    import pandas as pd
    df = pd.DataFrame(input_df)

    predicted_price = rf_model.predict(df)[0]

    return {
        "brand": request.brand,
        "year": request.year,
        "predicted_price": float(predicted_price)
    }
