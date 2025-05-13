import pickle
from sklearn.linear_model import LinearRegression
import numpy as np

# Données factices pour exemple
X = np.array([[50, 1, 0], [70, 2, 1], [100, 3, 2]])
y = np.array([150000, 250000, 300000])

# Entraînement d'un modèle simple
model = LinearRegression()
model.fit(X, y)

# Sauvegarde du modèle avec pickle
with open("regression_model.pkl", "wb") as f:
    pickle.dump(model, f)