# app/routes/predict.py

from fastapi import APIRouter
from app.services.predict_service import faire_prediction

router = APIRouter()

@router.post("/predict")
def predict(surface: float, chambres: int, quartier: str):
    prediction = faire_prediction(surface, chambres, quartier)
    return {"prediction": prediction}