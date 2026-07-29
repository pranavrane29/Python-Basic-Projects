import streamlit as st
import pandas as pd
import joblib


model = joblib.load("HousePriceModel.pkl")
scaler = joblib.load("HouseScaler.pkl")
encoded_columns = joblib.load("HouseColumns.pkl")

st.set_page_config(
    page_title="House Price Predictor",
    layout="centered"
)

st.title("House Price Predictor")

st.write("Enter the details below to predict the house price - ")

area = st.number_input(
    "Enter area (in Square_feet)",
    min_value=0,
    value=1000
)

bedrooms = st.number_input(
    "Enter number of Bedrooms - ",
    min_value=0,
    value=2
)

bathrooms = st.number_input(
    "Enter number of Bathrooms -  ",
    min_value=0,
    value= 1
)

stories = st.number_input(
    "Enter number of floors - ",
    min_value=0,
    value = 1
)

parking = st.number_input(
    "Enter number of parking space -",
    min_value=0,
    value = 1
)

mainroad = st.selectbox(
    "Is the house located on the mainroad?",
    ["yes","no"]
)

guestroom = st.selectbox(
    "Are there any guestrooms?",
    ["yes","no"]
)

basement = st.selectbox(
    "Does the house have the basement?",
    ["yes","no"]
)

hotwaterheating = st.selectbox(
    "Does the house have facility of hotwater?",
    ["yes","no"]
)

airconditioning = st.selectbox(
    "Does the house have air conditioning ?",
    ["yes","no"]
)

prefarea = st.selectbox(
    "Is the house located in the preferred area?",
    ["yes","no"]
)

furnishingstatus = st.selectbox(
    "What is the status of furnishing?",
    ["furnished","semi-furnished","unfurnished"]
)


if st.button("Predict Price") :
    try:
        input_data = pd.DataFrame({
            "area" : [area],
            "bedrooms" : [bedrooms],
            "bathrooms" : [bathrooms],
            "stories" : [stories],
            "mainroad" : [mainroad],
            "guestroom" : [guestroom],
            "basement" : [basement],
            "hotwaterheating" : [hotwaterheating],
            "airconditioning" : [airconditioning],
            "parking" : [parking],
            "prefarea" : [prefarea],
            "furnishingstatus" : [furnishingstatus]
        })

        input_data = pd.get_dummies(input_data)

        input_data = input_data.reindex(
            columns=encoded_columns,
            fill_value = 0
        )

        input_scaled = scaler.transform(input_data)

        st.divider()
        
        prediction = model.predict(input_scaled)

        st.success(f"Predicted House Price : Rs.{prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Error :{e}")

    st.divider()

    st.caption(
            "Model 1st of linear regression of task 23rd")
    st.caption(
        "Built using Streamlit, Scikit-learn and a Linear Regression Model by Pranav Rane.")