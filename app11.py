import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 1. Sayfa Yapılandırması
st.set_page_config(
    page_title="Graduation Predictor AI",
    page_icon="🎓",
    layout="wide"
)

# 2. Stil Düzenlemeleri (Hata düzeltildi: unsafe_allow_html)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .stButton>button { 
        width: 100%; 
        border-radius: 25px; 
        height: 3.5em; 
        background-color: #1e88e5; 
        color: white; 
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover { background-color: #1565c0; color: white; }
    </style>
    """, unsafe_allow_html=True)

# 3. Model Yükleme (Önbelleğe alarak hızı artırıyoruz)
@st.cache_resource
def load_model():
    # Model dosyanın isminin bu olduğundan emin ol!
    return joblib.load('student_success_model.pkl')

try:
    model = load_model()
except Exception as e:
    st.error(f"Model dosyası bulunamadı! Lütfen 'student_success_model.pkl' dosyasını yükleyin. Hata: {e}")

# 4. Üst Başlık ve Görsel
col_img, col_txt = st.columns([1, 1.5])

with col_img:
    st.image("https://img.freepik.com/premium-photo/student-climbing-stairs-made-books-with-cloudy-sky-background-symbolizing-education_1267554-302.jpg", 
             use_container_width=True)

with col_txt:
    st.title("🎓 Graduation Predictor AI")
    st.markdown("### *Empowering Education with Data Science*")
    st.write("""
    Bu sistem, öğrencinin demografik, sosyo-ekonomik ve akademik verilerini analiz ederek 
    mezuniyet durumunu tahmin eder. Optimize edilmiş **XGBoost** modeli kullanılarak 
    **%82.89** doğruluk oranıyla geliştirilmiştir.
    """)
    st.success("✅ Model Status: Active | Accuracy: 82.89%")

st.divider()

# 5. Kullanıcı Veri Girişi
st.subheader("📝 Student Profile Analysis")

with st.form("main_form"):
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.info("📊 Socio-Economic")
        scholarship = st.selectbox("Scholarship Holder", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
        debtor = st.selectbox("Financial Debtor", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
        tuition = st.selectbox("Tuition Fees Up to Date", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
        gender = st.selectbox("Gender", [0, 1], format_func=lambda x: "Male" if x==1 else "Female")
        age = st.number_input("Age at Enrollment", 15, 80, 20)

    with c2:
        st.info("📚 Academic History")
        attendance = st.selectbox("Attendance Mode", [0, 1], format_func=lambda x: "Daytime" if x==1 else "Evening")
        success_rate = st.slider("Success Rate (0 to 1)", 0.0, 1.0, 0.5)
        avg_grade = st.number_input("Average Grade", 0.0, 20.0, 12.0)
        admission_grade = st.number_input("Admission Grade", 0.0, 200.0, 120.0)

    with c3:
        st.info("⚙️ System Context")
        cluster = st.selectbox("K-Means Cluster", [0, 1, 2, 3])
        total_appr = st.number_input("Total Approved Units", 0, 30, 5)
        displaced = st.selectbox("Displaced (Migrant)", [0, 1])
        special_needs = st.selectbox("Special Needs", [0, 1])
        course_code = st.number_input("Course Code", 1, 9999, 1)

    submit = st.form_submit_button("PREDICT OUTCOME")

# 6. Sonuç ve Tahmin Ekranı
if submit:
    # Modelin beklediği tüm özellikler (Sıralama modelinle aynı olmalı)
    features = pd.DataFrame({
        'Marital status': [1], 'Application mode': [1], 'Application order': [1], 'Course': [course_code],
        'Daytime/evening attendance': [attendance], 'Previous qualification': [1], 
        'Previous qualification (grade)': [admission_grade], "Mother's qualification": [1],
        "Father's qualification": [1], "Mother's occupation": [1], "Father's occupation": [1],
        'Admission grade': [admission_grade], 'Displaced': [displaced], 
        'Educational special needs': [special_needs], 'Debtor': [debtor],
        'Tuition fees up to date': [tuition], 'Gender': [gender], 'Scholarship holder': [scholarship],
        'Age at enrollment': [age], 'Total_Approved': [total_appr], 
        'Total_Enrolled': [total_appr], 'Average_Grade': [avg_grade], 
        'Success_Rate': [success_rate], 'cluster': [cluster]
    })

    # Tahmin
    pred = model.predict(features)[0]
    prob = model.predict_proba(features)[0].max()
    
    # 0:Dropout, 1:Enrolled, 2:Graduate (LabelEncoder sırasına göre)
    labels = {0: ("Dropout 🔴", "High risk detected."), 
              1: ("Enrolled 🟡", "Student is in progress."), 
              2: ("Graduate 🟢", "High success potential!")}
    
    res_label, res_msg = labels[pred]

    st.divider()
    res1, res2 = st.columns(2)
    res1.metric("Predicted Status", res_label)
    res2.metric("Confidence Level", f"{prob*100:.2f}%")
    
    if pred == 2:
        st.balloons()
        st.success(res_msg)
    elif pred == 0:
        st.error(res_msg)
    else:
        st.warning(res_msg)
