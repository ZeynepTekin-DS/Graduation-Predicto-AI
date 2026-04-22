🚕 NYC Transit AI: Predictive Urban Mobility System

APPLICATION LINK (Hugging Face / GitHub):

https://huggingface.co/spaces/zeynepptkn/NYCTaxi-Duration-AI ---https://github.com/ZeynepTekin-DS/-NYCTaxi-Duration-AI

PROJECT SUMMARY: 📖
This study was developed to predict taxi trip durations within New York City’s complex transit network with high precision by analyzing urban mobility patterns. By examining the relationship between geographic coordinates and temporal data, the project transforms the dynamic nature of city traffic (peak hours, spatial density, etc.) into a mathematical model, moving beyond simple distance-based estimations.

METHODS USED:

XGBoost (Extreme Gradient Boosting): 🧠 In a benchmarking analysis conducted across eight different algorithms (Linear, Ridge, Lasso, etc.), "XGBoost" was selected as the champion model for its superior ability to capture complex, non-linear relationships. While linear models remained within the 40-47% range, XGBoost achieved significantly higher success by decoding urban traffic congestion.

Error Optimization: ⚖️ The target variable (trip_duration) was normalized using a "Logarithmic Transformation" (log1p). Bu balanced the variance caused by outliers (extremely long trips) and brought the model's predictive performance to a 79.23% R2 Score and a remarkably low 0.33 RMSE.

DATA PREPROCESSING:

Strategic Feature Engineering: 🖇️ Moving beyond raw data, new variables capturing the city’s "temporal pulse"—such as is_rush_hour (16:00–19:00), is_night (00:00–05:00), and day_of_week—were engineered. This allowed the model to distinguish between functional commuting hours and social mobility patterns.

Spatial Analysis: 🧹 To align with New York’s grid-based urban plan, both "Manhattan Distance" and "Haversine Distance" (dist_km) calculations were integrated. This taught the model to account for both straight-line distance and street-level spatial complexity.

Feature Selection: 🛠️ To eliminate data noise, irrelevant columns such as id, store_and_fwd_flag, and dropoff_datetime were removed, ensuring the model focused solely on high-impact signals.

KEY RESULTS:

Model Success: 🏆 The XGBoost model demonstrated consistent performance on test data, achieving an explainability rate of over 79%. These results prove that temporal features are just as critical as distance in urban mobility predictions.

Critical Insights: 📊 Analysis revealed that distance is not the only determinant of trip duration; factors such as traffic density (rush hour) and the day of the week increase predictive accuracy by more than 30%.

NOTES:

Interactive Interface: 🎨 Thanks to a minimalist interface designed with Streamlit, users can enter pickup and drop-off coordinates to receive real-time estimates of their trip duration in seconds or minutes, adjusted for traffic patterns.

Production Deployment: ☁️ The trained model (nyc_taxi_model.pkl) and the feature schema (feature_name.pkl) were deployed on Hugging Face, transforming raw data into an end-to-end AI product that provides instantaneous predictions.

Prepared by: Zeynep Tekin

Date: April 13, 2026