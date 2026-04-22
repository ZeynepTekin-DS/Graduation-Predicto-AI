import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 1. Page Configuration
st.set_page_config(page_title="NYC Taxi AI", page_icon="🚕", layout="centered")

# 2. Hero Image & Title
st.image("https://s.wsj.net/public/resources/images/BN-UV587_NYTAXI_TOP_20170827152144.jpg", use_container_width=True)
st.title("🚕 NYC Trip Duration Predictor")
st.markdown("Enter trip details below to estimate travel time using our **XGBoost AI Model**.")
st.divider()

# 3. Load Model and Features
@st.cache_resource
def load_assets():
    # Make sure these filenames match your saved files!
    model = joblib.load("nyc_taxi_model.pkl")
    features = joblib.load("feature_name.pkl")
    return model, features

model, features_list = load_assets()

# 4. User Inputs
st.subheader("📍 Trip Parameters")

# If they don't know coordinates, we use standard Manhattan defaults
with st.expander("🌐 Location Settings (Optional - Defaulted to Manhattan)", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        p_long = st.number_input("Pickup Longitude", value=-73.9857)
        p_lat = st.number_input("Pickup Latitude", value=40.7484)
    with col2:
        d_long = st.number_input("Dropoff Longitude", value=-73.9557)
        d_lat = st.number_input("Dropoff Latitude", value=40.7851)

# Main Inputs
col3, col4 = st.columns(2)
with col3:
    hour = st.slider("Hour of Day", 0, 23, 14)
    day = st.selectbox("Day of Week", options=[0,1,2,3,4,5,6], 
                       format_func=lambda x: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][x])
    rush_hour = st.toggle("Is it Rush Hour? (16:00 - 19:00)", value=False)

with col4:
    dist = st.number_input("Estimated Distance (km)", value=3.5, step=0.1)
    # If users don't know manhattan_dist, we can estimate it as 1.3x Euclidean or let them input
    man_dist = st.number_input("Manhattan Distance (km)", value=dist * 1.2)

# 5. Prediction Logic
st.divider()
if st.button("🚀 Calculate Estimated Time", use_container_width=True):
    # Prepare input array in the EXACT order of 'features_list'
    # features = ['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'hour', 'day_of_week', 'dist_km', 'manhattan_dist', 'is_rush_hour']
    
    input_data = pd.DataFrame([[p_long, p_lat, d_long, d_lat, hour, day, dist, man_dist, int(rush_hour)]],
                              columns=features_list)
    
    # Model Prediction
    log_pred = model.predict(input_data)
    total_seconds = np.expm1(log_pred[0])
    minutes = total_seconds / 60

    # Display Results
    st.balloons()
    st.success(f"### ⏱️ Estimated Trip Duration: {minutes:.2f} Minutes")
    st.metric(label="Total Seconds", value=f"{total_seconds:.0f}s")

