import streamlit as st
import pickle
import numpy as np

# Membaca model
diabetes_model = pickle.load(open("diabetesPredict.sav", "rb"))

# Judul
st.markdown("<h1 style='text-align: center;'>Diabetes Diagnosis</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Form inputan
input_container = st.container()

with input_container:
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.text_input("Kehamilan (Pregnancies)")

    with col2:
        Glucose = st.text_input("Glukosa (Glucose)")

    with col1:
        BloodPressure = st.text_input("Tekanan Darah (BloodPressure)")

    with col2:
        SkinThickness = st.text_input("Ketebalan Kulit (SkinThickness)")

    with col1:
        Insulin = st.text_input("Insulin (Insulin)")

    with col2:
        BMI = st.text_input("Indeks Massa Tubuh (BMI)")

    with col1:
        DiabetesPedigreeFunction = st.text_input("Riwayat Diabetes (DiabetesPedigreeFunction)")

    with col2:
        Age = st.text_input("Umur (Age)")

# Kode prediksi
diagnosis = " "

# Button prediksi
if st.button("Test"):
    data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]], dtype=np.float64)

    # Melakukan prediksi
    diagnosis = diabetes_model.predict(data)

    # Menampilkan hasil prediksi
    if diagnosis[0] == 1:
        prediksi = "Anda TERDETEKSI diabetes (You HAVE Diabetes)"
    else:
        prediksi = "Anda TIDAK TERDETEKSI diabetes (You DON'T HAVE Diabetes)"

    st.success(prediksi)
