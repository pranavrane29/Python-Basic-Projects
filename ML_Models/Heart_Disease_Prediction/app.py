import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

Base_Dir = Path(__file__).parent

model = joblib.load(Base_Dir/"heart_model.pkl")
scaler = joblib.load(Base_Dir/"scaler.pkl")
encoded_columns = joblib.load(Base_Dir/"columns.pkl")

st.set_page_config(
    page_title="Heart Disease Predictor",
    layout="centered"
)

st.title("Heart Disease Prediction System")

st.write("Enter the patients details below.")

age = st.number_input("Age",min_value=1,value=30)

sex = st.selectbox(
    "Sex",
    ["M","F"]
)

chestpain = st.selectbox(
    "Chest Pain Type",
    ["ATA","NAP","ASY","TA"]
)

restingbp = st.number_input(
    "Resting Blood Pressure",
    min_value=0,
    value=120
)

cholestrol = st.number_input(
    "Choloestrol",
    min_value=0,
    value=200
)

fastingbs = st.selectbox(
    "Fasting Blood Sugar",
    [0,1]
)

restingecg = st.selectbox(
    "Resting ECG",
    ["Normal","ST","LVH"]
)

maxhr = st.number_input(
    "Maximum Heart Rate",
    min_value=50,
    value=150
    )

exerciseanginga = st.selectbox(
    "Exercise Angina",
    ["Y","N"]
)

oldpeak = st.number_input(
    "Old Peak",
    value = 1.0
)

stslope = st.selectbox(
    "ST Slope",
    ["Up","Flat","Down"]
)

if st.button("Predict") :
    try:
        input_data = pd.DataFrame({
        "Age":[age],
        "Sex": [sex],
        "ChestPainType" : [chestpain],
        "RestingBP":[restingbp],
        "Cholesterol" : [cholestrol],
        "FastingBS" : [fastingbs],
        "RestingECG" : [restingecg],
        "MaxHR" : [maxhr],
        "ExerciseAngina" : [exerciseanginga],
        "Oldpeak" : [oldpeak],
        "ST_Slope" : [stslope]
        })

        input_data = pd.get_dummies(input_data)

        input_data = input_data.reindex(
            columns = encoded_columns,
            fill_value=0
        )

        input_scaled = scaler.transform(input_data)
        st.divider()
        prediction = model.predict(input_scaled)

        if prediction[0] == 1 :
            st.error("Heart Disease : YES")
        else :
            st.success("Heart Disease : NO")
    except Exception as e:
        st.error(f"Error :{e}")
        st.divider()
        st.caption(
        "Built using Streamlit, Scikit-learn and a Linear Regression Model by Pranav Rane.")