import streamlit as st
import pandas as pd
import joblib


#- Streamlit = Used this library for making web interface 
#- pandas = Used for making dataframes later
#- joblib = Used to deal with the opening and closing of model objects

#------------------------------------------------------------------------------------------------------

model = joblib.load("LR_ford_car.pkl")
scaler = joblib.load("scaler.pkl")
encoded_columns = joblib.load("columns.pkl")

#------------------------------------------------------------------------------------------------------


st.set_page_config(
    page_title="Ford Car Price Predictor",
    layout="centered"
)
#By using this code we set the page title of the website and set layout as centered
#for when the rendering happens, it would render in center

#------------------------------------------------------------------------------------------------------

st.title("Ford Car Price Predictor")

st.write("Enter the details below to predict the cars price - ")

st.header("🚗 Car Details")
#------------------------------------------------------------------------------------------------------


year = st.number_input(
    "Manufacturing Year",
    min_value=1990,
    max_value=2026,
    value=2018
)

mileage = st.number_input(
    "Mileage",
    min_value=0,
    value=20000
)

tax = st.number_input(
    "Road Tax",
    min_value=0,
    value = 150
)

mpg = st.number_input(
    "MPG",
    min_value=0.0,
    value=50.0
)

engineSize = st.number_input(
    "Engine Size",
    min_value=0.0,
    value=1.5
)

#------------------------------------------------------------------------------------------------------

transmission = st.selectbox(
    "Transmission",
    ["Automatic","Manual","Semi-Auto"]
)

fuelType = st.selectbox(
    "Fuel Type",
    ["Petrol","Diesel","Hybrid","Electric","Other"]
)


# The advantage of using selectbox() is that we can restrict the user for the choice they have.
# We only want the user to input values that are available and it also make the interface attractive.
# Either way we do not want the user to type "Gear wale gadi" in transmisson type xD......


#------------------------------------------------------------------------------------------------------

model_name = st.text_input("Car Model Name")
if model_name.strip() == "":
    st.warning("Please enter the car model name.")
else :
    if st.button("Predict Price") :
        try :
            st.write("Price Predicted!")


#------------------------------------------------------------------------------------------------------


            input_data = pd.DataFrame({
                    "model":[model_name],
                    "year" : [year],
                    "transmission" : [transmission],
                    "mileage" : [mileage],
                    "fuelType" : [fuelType],
                    "tax" : [tax],
                    "mpg" : [mpg],
                    "engineSize" : [engineSize]
                })

            input_encoded = pd.get_dummies(
                input_data,columns=["model","transmission","fuelType"],dtype=int
            )

                

            input_encoded = input_encoded.reindex(
                columns=encoded_columns,
                fill_value=0
            )


#------------------------------------------------------------------------------------------------------
                
            numeric_cols = ["year", "mileage", "tax", "mpg", "engineSize"]

            input_encoded[numeric_cols] = scaler.transform(input_encoded[numeric_cols])

            st.divider()

            predicted_price = model.predict(input_encoded)


            st.success(f"Estimated Selling Price: £{predicted_price[0]:,.2f}")

        except Exception as e:
            st.error(f"Error: {e}")

        
        st.divider()

        st.caption(
            "Built using Streamlit, Scikit-learn and a Linear Regression Model by Pranav Rane.")
        
