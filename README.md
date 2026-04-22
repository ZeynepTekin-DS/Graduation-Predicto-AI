🎓 Graduation Predictor AI: Academic Success and Student Dropout Analysis System

APPLICATION LINK (Hugging Face):

 https://huggingface.co/spaces/zeynepptkn/Graduation-Predicto-AI --https://github.com/ZeynepTekin-DS/Graduation-Predicto-AI

PROJECT SUMMARY: 📖 This study was developed to predict graduation success or dropout risks with high precision by analyzing students' academic backgrounds and socio-economic conditions. By blending critical data such as financial stability, demographic attributes, and semester grades, the project provides an early-warning decision-support system for educational institutions.
METHODS USED:

Advanced Ensemble Learning (XGBoost): 🧠 The optimized XGBoost algorithm was utilized to capture complex and non-linear relationships within the student lifecycle. The model was refined through hyperparameter optimization to minimize classification complexity and maximize efficiency.

Performance Stability: ⚖️ The model achieved a high level of success with an 82.89% Accuracy rate. The minimal difference between Accuracy and F1 scores proves that the system is robust and generates reliable predictions on new profiles without overfitting.

Hybrid Analysis (K-Means Integration): 🧬 Unsupervised learning (K-Means) was used to identify "hidden student archetypes" that traditional models might overlook. These clustered structures were transformed into features that support the model's predictive power by over 90%.
DATA PREPROCESSING & FEATURE ENGINEERING:

Socio-Economic Feature Engineering: 🖇️ New variables were derived from raw data within a sociological logic framework—such as financial debt status, scholarship availability, and tuition fee up-to-dateness—which directly impact academic success.

Multicollinearity & Cleaning: 🧹 Redundant (multicollinear) structures from multi-semester metrics were cleaned to ensure a leaner and faster model. Factors with low statistical impact, such as nationality and international status, were eliminated to optimize the model architecture.

Data Scaling & Encoding: 🛠️ Categorical data (Graduate/Dropout/Enrolled) were converted into numerical values, and all features were standardized for the fastest convergence of the XGBoost algorithm.
KEY RESULTS:

High Precision Prediction: 🏆 The developed system has reached the capacity to predict a student's future before they even graduate. It demonstrates near-perfect success in distinguishing between extreme scenarios such as "Graduate" and "Dropout."

Critical Insights: 📊 Analysis proved that the most critical factors in academic success are Scholarship Status, Financial Debt, and Payment Up-to-dateness. Furthermore, it was statistically documented that female students tend to have higher academic performance stability.
NOTES:

Interactive Interface: 🎨 Thanks to the user-friendly interface developed with Streamlit, users can enter details such as age, gender, scholarship status, and GPA to receive the student's "graduation probability" and "confidence rate" within seconds.

Production Deployment: ☁️ The trained model was packaged in .joblib format and deployed live on Hugging Face Spaces, transforming complex educational data into an end-to-end AI product providing strategic insights.

    [!IMPORTANT]

    Model Storage Notice: Due to GitHub's file size limits, the trained model file is hosted on Hugging Face. You can access the fully functional application and the model via the link provided at the top of this page.

Prepared By: Zeynep Tekin

Date: April 11, 2026