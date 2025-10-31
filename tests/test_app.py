# tests/test_app.py
from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

def test_health_check():
    """Vérifie que /health retourne status ok"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict_route():
    """Vérifie que /predict fonctionne"""
    payload = {
        "brand": "Toyota",
        "model": "Corolla",
        "year": 2020,
        "mileage": 35000
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "predicted_price" in data


# tests/test_app.py
def test_predict_real():
    payload = {
        "brand": "Maruti",
        "year": 2014,
        "owner": "First",
        "fuel": "Diesel",
        "seller_type": "Individual",
        "transmission": "Manual",
        "km_driven": 145500,
        "mileage_mpg": 55.0,
        "engine_cc": 1248.0,
        "max_power_bhp": 74.0,
        "torque_nm": 190.0,
        "seats": 5.0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "predicted_price" in data
    assert data["predicted_price"] > 0

