from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.predict_service import faire_prediction

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict_form", response_class=HTMLResponse)
def predict_form(request: Request, surface: float = Form(...), chambres: int = Form(...), quartier: str = Form(...)):
    input_data = {"surface": surface, "chambres": chambres, "quartier": quartier}
    result = faire_prediction(input_data)
    return templates.TemplateResponse("index.html", {"request": request, "prediction": result})