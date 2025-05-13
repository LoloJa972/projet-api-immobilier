from fastapi import FastAPI, Request, Form, Body
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from app.services.predict_service import faire_prediction

app = FastAPI()

# Configuration Jinja2
templates = Jinja2Templates(directory="templates")

# Page HTML avec formulaire
@app.get("/", response_class=HTMLResponse)
def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Soumission du formulaire HTML
@app.post("/predict_form", response_class=HTMLResponse)
def predict_form(
    request: Request,
    surface: float = Form(...),
    chambres: int = Form(...),
    quartier: str = Form(...)
):
    input_data = {
        "surface": surface,
        "chambres": chambres,
        "quartier": quartier
    }
    prediction = faire_prediction(input_data)
    return templates.TemplateResponse("index.html", {"request": request, "prediction": prediction})

# Endpoint JSON pour API / Power BI
class PredictionInput(BaseModel):
    surface: float
    chambres: int
    quartier: str

@app.post("/predict")
def predict_api(input_data: PredictionInput):
    prediction = faire_prediction(input_data.dict())
    return {"prediction": prediction}