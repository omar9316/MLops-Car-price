# 🚗 MLops Car Price Predictor

Projet MLOps complet pour prédire le prix des voitures avec **FastAPI**, **Streamlit** et **Docker**.  
Il inclut un backend ML, un frontend interactif et une orchestration Docker.


## ⚙️ Installation locale

1. Cloner le dépôt :

```bash
git clone https://github.com/omar9316/MLops-Car-price.git
cd MLops-Car-price
Créer un environnement virtuel Python :

bash
Copier le code
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
Installer les dépendances :

bash
Copier le code
pip install -r requirements.txt


🐳 Lancer avec Docker
Construire et lancer les containers :

bash
Copier le code
docker-compose up --build
Vérifier que les services sont actifs :

Frontend : http://localhost:8501

Backend : http://localhost:8000


