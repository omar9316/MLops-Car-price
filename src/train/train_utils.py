# src/train/train_utils.py
import os

# Chemin vers le fichier CSV (dossier racine)
DATA_FILE_PATH = os.path.join(os.getcwd(), "car-details.csv")

# Répertoire où le modèle sera sauvegardé
MODEL_DIR = os.path.join(os.getcwd(), "models")
MODEL_PATH = os.path.join(MODEL_DIR, "rf_model.joblib")
