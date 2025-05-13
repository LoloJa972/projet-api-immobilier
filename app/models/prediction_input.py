from pydantic import BaseModel

class PredictionInput(BaseModel):
    surface: float
    chambres: int
    quartier: str