# 🚗 MLops Car Price Predictor

Projet MLOps complet pour prédire le prix des voitures avec **FastAPI**, **Streamlit** et **Docker**.  
Il inclut un backend ML, un frontend interactif et une orchestration Docker.

---

## 📁 Structure du projet

MLops-Car-price/
│
├─ src/ # Code backend FastAPI
│ ├─ app/
│ ├─ pipeline/
│ ├─ train/
│ └─ ...
│
├─ models/ # Modèle ML entraîné (rf_model.joblib)
├─ frontend.py # Interface utilisateur Streamlit
├─ Dockerfile # Dockerfile backend
├─ Dockerfile.frontend # Dockerfile frontend
├─ docker-compose.yml # Orchestration des services
├─ requirements.txt # Dépendances Python
├─ car-details.csv # Dataset
└─ README.md

yaml
Copier le code

---

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
🏗️ Lancer le projet localement
1. Entraîner le modèle
bash
Copier le code
python -m src.train.train_model
2. Lancer le backend FastAPI
bash
Copier le code
uvicorn src.app.main:app --reload
3. Lancer le frontend Streamlit
bash
Copier le code
streamlit run frontend.py
Le frontend sera accessible sur http://localhost:8501
Le backend FastAPI sur http://localhost:8000

🐳 Lancer avec Docker
Construire et lancer les containers :

bash
Copier le code
docker-compose up --build
Vérifier que les services sont actifs :

Frontend : http://localhost:8501

Backend : http://localhost:8000

📝 Fonctionnalités
Prédiction du prix d’une voiture à partir de ses caractéristiques

Backend FastAPI dockerisé

Frontend Streamlit dockerisé

Communication frontend ↔ backend via Docker Compose

Tests unitaires avec pytest

Modèle ML entraîné avec RandomForestRegressor

Structure de projet modulable pour MLOps

🔧 Tests unitaires
Pour vérifier que tout fonctionne :

bash
Copier le code
python -m pytest -q
📌 Bonnes pratiques incluses
Environnement virtuel .venv

.gitignore pour ne pas versionner les fichiers temporaires

Dockerfile pour backend et frontend

Docker Compose pour orchestration

Fichiers de configuration Streamlit

👤 Auteur
Omar Hitar - GitHub

📸 Capture d’écran
(Ajouter ici un screenshot de ton frontend si tu veux embellir le README)

yaml
Copier le code

---

Si tu veux, je peux aussi te préparer **une version “README visuel avec images et badges”** pour qu’il soit très pro, comme les vrais projets open-source MLOps.  

Veux‑tu que je fasse ça ?