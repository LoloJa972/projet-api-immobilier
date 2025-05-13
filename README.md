# 🏠 Projet API de Prédiction Immobilière

Ce projet est une API web simple basée sur **FastAPI** qui permet de prédire le prix d’un bien immobilier selon plusieurs caractéristiques :
- Surface (en m²)
- Nombre de pièces
- Distance au centre-ville
- Quartier (dans la version avec formulaire HTML)

---

## 🚀 Fonctionnalités

- 🔢 Endpoint `/predict` : API REST prenant un JSON en entrée
- 🌐 Formulaire HTML interactif à l'adresse `/form`
- 🤖 Modèle de régression simple pour la prédiction
- 📦 Emballé dans un projet modulaire et prêt pour Docker

---

## 🛠️ Stack technique

- Python 3.11
- FastAPI
- Uvicorn
- Jinja2 (formulaire HTML)
- Pickle (modèle ML simple)
- SQLite (optionnel pour données persistantes)

---

## ▶️ Démarrer le projet localement

### 1. Cloner le dépôt

```bash
git clone https://github.com/<ton-utilisateur>/projet-api-prediction.git
cd projet-api-prediction
