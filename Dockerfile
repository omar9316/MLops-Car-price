# --- Étape 1 : image de base Python ---
FROM python:3.10-slim

# --- Étape 2 : variables d'environnement ---
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# --- Étape 3 : créer le dossier de travail ---
WORKDIR /app

# --- Étape 4 : copier les fichiers nécessaires ---
COPY requirements.txt ./
COPY src ./src
COPY models ./models

# --- Étape 5 : installer les dépendances ---
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# --- Étape 6 : exposer le port de l'API ---
EXPOSE 8000

# --- Étape 7 : commande pour lancer le serveur ---
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
