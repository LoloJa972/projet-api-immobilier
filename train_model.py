import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

# Création du dossier 'model' s'il n'existe pas
os.makedirs("model", exist_ok=True)

# Jeu de données d'entraînement (exemple simplifié)
data = pd.DataFrame({
    "surface": [50, 70, 100, 120],
    "chambres": [1, 2, 3, 4],
    "quartier": ["centre", "sud", "nord", "est"],
    "prix": [200000, 280000, 350000, 420000]
})

# Encodage simple du quartier (hash mod 1000)
data["quartier_encoded"] = data["quartier"].apply(lambda q: hash(q) % 1000)

# Variables explicatives et cible
X = data[["surface", "chambres", "quartier_encoded"]]
y = data["prix"]

# Entraînement d'un modèle de régression linéaire
model = LinearRegression()
model.fit(X, y)

# Sauvegarde du modèle
joblib.dump(model, "model/regression_model.pkl")
print("✅ Modèle entraîné et sauvegardé dans 'model/regression_model.pkl'")