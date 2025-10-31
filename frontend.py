import streamlit as st
import requests
import os

# API_URL = "http://localhost:8000"  # Ton backend Dockerisé
API_URL = os.getenv("API_URL", "http://localhost:8000")
API_KEY = os.getenv("API_KEY", "demo-key")  # Optionnel


# --- Page Setup ---
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)
st.title("🚗 Car Price Prediction")

# --- Prediction Interface ---
st.header("Enter Car Details to Predict Price")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        company = st.selectbox(
            "Brand",
            sorted(['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault', 'Mahindra',
                    'Tata', 'Chevrolet', 'Fiat', 'Datsun', 'Jeep', 'Mercedes-Benz', 'Mitsubishi',
                    'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus', 'Jaguar', 'Land', 'MG', 'Volvo',
                    'Daewoo', 'Kia', 'Force', 'Ambassador', 'Ashok', 'Isuzu', 'Opel', 'Peugeot'])
        )
        year = st.number_input("Manufacturing Year", min_value=1990, max_value=2024, value=2015)
        km_driven = st.number_input("Kilometers Driven", min_value=0, value=50000)
        fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG"])
        seller_type = st.selectbox("Seller Type", ["Individual", "Dealer", "Trustmark Dealer"])
        transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

    with col2:
        owner = st.selectbox("Owner", ["First", "Second", "Third", "Fourth & Above", "Test Drive Car"])
        mileage_mpg = st.number_input("Mileage (in MPG)", min_value=5.0, max_value=60.0, value=20.0)
        engine_cc = st.number_input("Engine (in CC)", min_value=600, max_value=6000, value=1500)
        max_power_bhp = st.number_input("Max Power (in BHP)", min_value=30.0, max_value=600.0, value=90.0)
        torque_nm = st.number_input("Torque (in Nm)", min_value=40.0, max_value=800.0, value=150.0)
        seats = st.number_input("Number of Seats", min_value=2, max_value=10, value=5)

    submit = st.form_submit_button("Calculate Price")

if submit:
    input_data = {
        "brand": company,
        "year": year,
        "owner": owner,
        "fuel": fuel,
        "seller_type": seller_type,
        "transmission": transmission,
        "km_driven": float(km_driven),
        "mileage_mpg": float(mileage_mpg),
        "engine_cc": float(engine_cc),
        "max_power_bhp": float(max_power_bhp),
        "torque_nm": float(torque_nm),
        "seats": float(seats)
    }

    try:
        response = requests.post(f"{API_URL}/predict", json=input_data)
        if response.status_code == 200:
            price = response.json().get("predicted_price")
            st.success(f"### Predicted Price: ₹ {price}")
        else:
            st.error(f"Prediction failed. Status code: {response.status_code}")
            st.json(response.json())
    except requests.exceptions.RequestException as e:
        st.error(f"Could not connect to API: {e}")
