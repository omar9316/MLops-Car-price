# src/app/main.py
from fastapi import FastAPI
from src.app.routes import router  # import des routes depuis routes.py

# Crée l'application FastAPI
app = FastAPI(
    title="Car Price Prediction API",
    description="API pour prédire le prix des voitures d'occasion",
    version="1.0.0",
)

# Enregistre les routes définies dans routes.py
app.include_router(router)


# Lancer le serveur depuis le terminal avec :
# uvicorn src.app.main:app --reload
