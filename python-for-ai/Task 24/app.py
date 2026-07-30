import os

import joblib
import pandas as pd
import streamlit as st

from preprocessing import (
    build_house_row,
    build_hotel_row,
    HOUSE_FURNISHING_OPTIONS,
    HOTEL_TYPE_OPTIONS,
    MONTH_OPTIONS,
    MEAL_OPTIONS,
    MARKET_SEGMENT_OPTIONS,
    DISTRIBUTION_CHANNEL_OPTIONS,
    DEPOSIT_TYPE_OPTIONS,
    CUSTOMER_TYPE_OPTIONS,
    get_country_options,
    get_reserved_room_options,
    get_assigned_room_options,
)

MODELS_DIR = os.path.join(os.path.dirname(__file__), "models")

st.set_page_config(page_title="ML Prediction Studio", page_icon="📊", layout="centered")


@st.cache_resource
def load_house_artifacts():
    model = joblib.load(os.path.join(MODELS_DIR, "HousePriceModel__2_.pkl"))
    scaler = joblib.load(os.path.join(MODELS_DIR, "HouseScaler__2_.pkl"))
    columns = joblib.load(os.path.join(MODELS_DIR, "HouseColumns__2_.pkl"))
    return model, scaler, columns


@st.cache_resource
def load_hotel_artifacts():
    model = joblib.load(os.path.join(MODELS_DIR, "hotel_booking_model__2_.pkl"))
    scaler = joblib.load(os.path.join(MODELS_DIR, "hotelscaler.pkl"))
    columns = list(joblib.load(os.path.join(MODELS_DIR, "hotelcolumns.pkl")))
    return model, scaler, columns


st.title("📊 ML Prediction Studio")
st.caption(
    "Loads your saved models/scalers/column files directly — no retraining, "
    "no placeholder logic."
)

problem_type = st.sidebar.radio("1. Choose problem type", ["Regression", "Classification"])

st.sidebar.markdown("---")
st.sidebar.subheader("2. Select algorithm")

# -----------------------------------------------------------------------
# REGRESSION -> House price model
# -----------------------------------------------------------------------
if problem_type == "Regression":
    model, scaler, columns = load_house_artifacts()
    algo_name = type(model).__name__
    st.sidebar.selectbox(
        "Trained regression model available",
        [algo_name],
        disabled=True,
        help="Only one regression model was saved (HousePriceModel). "
        "No other trained regression algorithms were provided.",
    )

    st.header("🏠 House Price Prediction")
    st.write(f"Model: **{algo_name}**")

    col1, col2 = st.columns(2)
    with col1:
        area = st.number_input("Area (sq ft)", min_value=100, max_value=100000, value=5000, step=50)
        bedrooms = st.number_input("Bedrooms", min_value=0, max_value=20, value=3, step=1)
        bathrooms = st.number_input("Bathrooms", min_value=0, max_value=20, value=2, step=1)
        stories = st.number_input("Stories", min_value=1, max_value=10, value=2, step=1)
        parking = st.number_input("Parking spaces", min_value=0, max_value=10, value=1, step=1)
        furnishingstatus = st.selectbox("Furnishing status", HOUSE_FURNISHING_OPTIONS)

    with col2:
        mainroad = st.selectbox("On main road?", ["yes", "no"])
        guestroom = st.selectbox("Has guest room?", ["yes", "no"])
        basement = st.selectbox("Has basement?", ["yes", "no"])
        hotwaterheating = st.selectbox("Has hot water heating?", ["yes", "no"])
        airconditioning = st.selectbox("Has air conditioning?", ["yes", "no"])
        prefarea = st.selectbox("In preferred area?", ["yes", "no"])

    if st.button("Predict price", type="primary"):
        raw = dict(
            area=area, bedrooms=bedrooms, bathrooms=bathrooms, stories=stories,
            parking=parking, mainroad=mainroad, guestroom=guestroom, basement=basement,
            hotwaterheating=hotwaterheating, airconditioning=airconditioning,
            prefarea=prefarea, furnishingstatus=furnishingstatus,
        )
        row_df = build_house_row(raw, columns)
        scaled = scaler.transform(row_df)
        prediction = model.predict(scaled)[0]
        st.success(f"### Predicted price: ₹{prediction:,.2f}")
        with st.expander("See feature vector sent to the model"):
            st.dataframe(row_df)

# -----------------------------------------------------------------------
# CLASSIFICATION -> Hotel booking cancellation model
# -----------------------------------------------------------------------
else:
    model, scaler, columns = load_hotel_artifacts()
    algo_name = type(model).__name__
    st.sidebar.selectbox(
        "Trained classification model available",
        [algo_name],
        disabled=True,
        help="Only one classification model was saved (hotel_booking_model). "
        "No other trained classification algorithms were provided.",
    )

    st.header("🏨 Hotel Booking Cancellation Prediction")
    st.write(f"Model: **{algo_name}**")

    with st.form("hotel_form"):
        st.subheader("Stay details")
        c1, c2, c3 = st.columns(3)
        with c1:
            hotel = st.selectbox("Hotel type", HOTEL_TYPE_OPTIONS)
            arrival_date_year = st.number_input("Arrival year", min_value=2015, max_value=2035, value=2017)
            arrival_date_month = st.selectbox("Arrival month", MONTH_OPTIONS)
            arrival_date_week_number = st.number_input("Arrival week number", 1, 53, 27)
            arrival_date_day_of_month = st.number_input("Arrival day of month", 1, 31, 15)
        with c2:
            lead_time = st.number_input("Lead time (days)", 0, 800, 50)
            stays_in_weekend_nights = st.number_input("Weekend nights", 0, 20, 1)
            stays_in_week_nights = st.number_input("Week nights", 0, 40, 2)
            adults = st.number_input("Adults", 0, 10, 2)
            children = st.number_input("Children", 0, 10, 0)
        with c3:
            babies = st.number_input("Babies", 0, 10, 0)
            is_repeated_guest = st.selectbox("Repeated guest?", [0, 1])
            previous_cancellations = st.number_input("Previous cancellations", 0, 50, 0)
            previous_bookings_not_canceled = st.number_input("Previous bookings not canceled", 0, 100, 0)
            booking_changes = st.number_input("Booking changes", 0, 30, 0)

        st.subheader("Booking economics & room")
        c4, c5, c6 = st.columns(3)
        with c4:
            days_in_waiting_list = st.number_input("Days in waiting list", 0, 400, 0)
            adr = st.number_input("Average Daily Rate (ADR)", 0.0, 5000.0, 100.0, step=1.0)
            required_car_parking_spaces = st.number_input("Required car parking spaces", 0, 8, 0)
            total_of_special_requests = st.number_input("Total special requests", 0, 10, 0)
        with c5:
            meal = st.selectbox("Meal plan", MEAL_OPTIONS)
            country = st.selectbox("Country", get_country_options(columns))
            market_segment = st.selectbox("Market segment", MARKET_SEGMENT_OPTIONS)
            distribution_channel = st.selectbox("Distribution channel", DISTRIBUTION_CHANNEL_OPTIONS)
        with c6:
            reserved_room_type = st.selectbox("Reserved room type", get_reserved_room_options(columns))
            assigned_room_type = st.selectbox("Assigned room type", get_assigned_room_options(columns))
            deposit_type = st.selectbox("Deposit type", DEPOSIT_TYPE_OPTIONS)
            customer_type = st.selectbox("Customer type", CUSTOMER_TYPE_OPTIONS)

        submitted = st.form_submit_button("Predict cancellation", type="primary")

    if submitted:
        raw = dict(
            hotel=hotel, arrival_date_year=arrival_date_year, arrival_date_month=arrival_date_month,
            arrival_date_week_number=arrival_date_week_number,
            arrival_date_day_of_month=arrival_date_day_of_month, lead_time=lead_time,
            stays_in_weekend_nights=stays_in_weekend_nights, stays_in_week_nights=stays_in_week_nights,
            adults=adults, children=children, babies=babies, is_repeated_guest=is_repeated_guest,
            previous_cancellations=previous_cancellations,
            previous_bookings_not_canceled=previous_bookings_not_canceled,
            booking_changes=booking_changes, days_in_waiting_list=days_in_waiting_list, adr=adr,
            required_car_parking_spaces=required_car_parking_spaces,
            total_of_special_requests=total_of_special_requests, meal=meal, country=country,
            market_segment=market_segment, distribution_channel=distribution_channel,
            reserved_room_type=reserved_room_type, assigned_room_type=assigned_room_type,
            deposit_type=deposit_type, customer_type=customer_type,
        )
        row_df = build_hotel_row(raw, columns)
        scaled = scaler.transform(row_df)
        prediction = model.predict(scaled)[0]
        proba = model.predict_proba(scaled)[0]

        if prediction == 1:
            st.error(f"### Prediction: Booking likely to be CANCELED (probability {proba[1]:.1%})")
        else:
            st.success(f"### Prediction: Booking likely to be HONORED (probability {proba[0]:.1%})")

        with st.expander("See feature vector sent to the model"):
            st.dataframe(row_df)
