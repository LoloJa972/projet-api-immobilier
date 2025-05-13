import pickle
import os

# Chemin du modèle entraîné
MODEL_PATH = "regression_model.pkl"

# Charger le modèle au lancement
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

def faire_prediction(input_data: dict) -> str:
    surface = input_data["surface"]
    chambres = input_data["chambres"]
    quartier = input_data["quartier"]

    # Exemple simple : on encode le quartier manuellement
    quartier_map = {"centre": 0, "sud": 1, "nord": 2}
    quartier_encoded = quartier_map.get(quartier.lower(), 0)

    # Faire une prédiction
    X = [[surface, chambres, quartier_encoded]]
    prediction = model.predict(X)[0]
    return f"Prix estimé : {prediction:.2f} €"