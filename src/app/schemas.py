# src/app/schemas.py
from pydantic import BaseModel

class PredictionRequest(BaseModel):
    brand: str
    year: int
    owner: str
    fuel: str
    seller_type: str
    transmission: str
    km_driven: float
    mileage_mpg: float
    engine_cc: float
    max_power_bhp: float
    torque_nm: float
    seats: float
