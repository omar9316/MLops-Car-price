# src/train/train_model.py
import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

from src.pipeline.preprocess import build_preprocessor
from src.train.train_utils import DATA_FILE_PATH, MODEL_DIR, MODEL_PATH

def load_data():
    """Charge le CSV et supprime les colonnes inutiles"""
    df = (
        pd.read_csv(DATA_FILE_PATH)
        .drop_duplicates()
        .drop(columns=['name', 'model', 'edition'], errors='ignore')
    )
    X = df.drop(columns='selling_price')
    y = df['selling_price'].copy()
    return X, y

def train_and_save_model():
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    preprocessor = build_preprocessor(X_train)
    regressor = RandomForestRegressor(n_estimators=10, max_depth=5, random_state=42)

    model_pipeline = Pipeline(steps=[
        ('pre', preprocessor),
        ('reg', regressor)
    ])

    model_pipeline.fit(X_train, y_train)

    # Créer dossier models si nécessaire
    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(model_pipeline, MODEL_PATH)
    print(f"Modèle sauvegardé dans : {MODEL_PATH}")

if __name__ == "__main__":
    train_and_save_model()
