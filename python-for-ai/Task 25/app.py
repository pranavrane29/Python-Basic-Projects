import streamlit as st
import pandas as pd
import joblib

model = joblib.load("best_model.pkl")
columns = joblib.load("columns.pkl")
label = joblib.load("label_encoder.pkl")

st.title("Penguin Species Prediction")

bill_length_mm = st.number_input("Bill Length (mm)",30.0,60.0,45.0)
bill_depth_mm = st.number_input("Bill Depth (mm)",10.0,25.0,17.0)
flipper_length_mm = st.number_input("Flipper Length (mm)",150.0,250.0,200.0)
body_mass_g = st.number_input("Body Mass (g)",2500.0,6500.0,4000.0)

sex = st.selectbox("Sex",["Male","Female"])

island = st.selectbox(
"Island",
["Biscoe","Dream","Torgersen"]
)

data = {
"bill_length_mm":bill_length_mm,
"bill_depth_mm":bill_depth_mm,
"flipper_length_mm":flipper_length_mm,
"body_mass_g":body_mass_g,
"island_Dream":0,
"island_Torgersen":0,
"sex_Male":0
}

if island=="Dream":
    data["island_Dream"]=1

elif island=="Torgersen":
    data["island_Torgersen"]=1

if sex=="Male":
    data["sex_Male"]=1

df = pd.DataFrame([data])

df = df.reindex(columns=columns,fill_value=0)

if st.button("Predict"):

    prediction=model.predict(df)

    st.success(
        label.inverse_transform(prediction)[0]
    )