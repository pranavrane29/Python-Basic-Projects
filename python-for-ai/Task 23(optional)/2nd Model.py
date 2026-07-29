import streamlit as st
import pandas as pd
import joblib

# Load saved files
model = joblib.load("hotel_booking_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

# Page settings
st.set_page_config(
    page_title="Hotel Booking Cancellation Prediction",
    page_icon="🏨",
    layout="wide"
)

st.title("🏨 Hotel Booking Cancellation Prediction")
st.write("Fill in the booking details below to predict whether the booking is likely to be cancelled.")

st.header("📅 Booking Information")

hotel = st.selectbox(
    "Hotel Type",
    ["City Hotel", "Resort Hotel"]
)

lead_time = st.number_input(
    "Lead Time (Days)",
    min_value=0,
    value=30
)

arrival_date_year = st.selectbox(
    "Arrival Year",
    [2015, 2016, 2017]
)

arrival_date_month = st.selectbox(
    "Arrival Month",
    [
        "January","February","March","April","May","June",
        "July","August","September","October","November","December"
    ]
)

arrival_date_week_number = st.slider(
    "Arrival Week Number",
    1,
    53,
    25
)

arrival_date_day_of_month = st.slider(
    "Arrival Day",
    1,
    31,
    15
)



st.header("👨 Guest Information")

adults = st.number_input(
    "Adults",
    min_value=1,
    value=2
)

children = st.number_input(
    "Children",
    min_value=0,
    value=0
)

babies = st.number_input(
    "Babies",
    min_value=0,
    value=0
)

is_repeated_guest = st.selectbox(
    "Repeated Guest",
    [0,1]
)


st.header("🛏 Stay Information")

stays_in_weekend_nights = st.number_input(
    "Weekend Nights",
    min_value=0,
    value=1
)

stays_in_week_nights = st.number_input(
    "Week Nights",
    min_value=0,
    value=2
)

meal = st.selectbox(
    "Meal Plan",
    [
        "BB",
        "HB",
        "FB",
        "SC",
        "Undefined"
    ]
)


st.header("🌍 Booking Details")

country = st.selectbox(
    "Country",
    [
        "PRT", "GBR", "ESP", "FRA",
        "DEU", "ITA", "USA", "BRA",
        "Other"
    ]
)

market_segment = st.selectbox(
    "Market Segment",
    [
        "Direct",
        "Corporate",
        "Online TA",
        "Offline TA/TO",
        "Complementary",
        "Groups",
        "Aviation"
    ]
)

distribution_channel = st.selectbox(
    "Distribution Channel",
    [
        "Direct",
        "Corporate",
        "TA/TO",
        "GDS"
    ]
)

previous_cancellations = st.number_input(
    "Previous Cancellations",
    min_value=0,
    value=0
)

previous_bookings_not_canceled = st.number_input(
    "Previous Bookings Not Cancelled",
    min_value=0,
    value=0
)


st.header("🛏 Room Information")

reserved_room_type = st.selectbox(
    "Reserved Room Type",
    list("ABCDEFGHIJKL")
)

assigned_room_type = st.selectbox(
    "Assigned Room Type",
    list("ABCDEFGHIJKLP")
)

st.header("💳 Payment & Customer")

booking_changes = st.number_input(
    "Booking Changes",
    min_value=0,
    value=0
)

deposit_type = st.selectbox(
    "Deposit Type",
    [
        "No Deposit",
        "Non Refund",
        "Refundable"
    ]
)

customer_type = st.selectbox(
    "Customer Type",
    [
        "Transient",
        "Transient-Party",
        "Contract",
        "Group"
    ]
)

adr = st.number_input(
    "Average Daily Rate (ADR)",
    min_value=0.0,
    value=100.0
)

required_car_parking_spaces = st.slider(
    "Required Parking Spaces",
    0,
    5,
    0
)

total_of_special_requests = st.slider(
    "Special Requests",
    0,
    5,
    1
)


sample = pd.DataFrame({
    "hotel": [hotel],
    "lead_time": [lead_time],
    "arrival_date_year": [arrival_date_year],
    "arrival_date_month": [arrival_date_month],
    "arrival_date_week_number": [arrival_date_week_number],
    "arrival_date_day_of_month": [arrival_date_day_of_month],
    "stays_in_weekend_nights": [stays_in_weekend_nights],
    "stays_in_week_nights": [stays_in_week_nights],
    "adults": [adults],
    "children": [children],
    "babies": [babies],
    "meal": [meal],
    "country": [country],
    "market_segment": [market_segment],
    "distribution_channel": [distribution_channel],
    "is_repeated_guest": [is_repeated_guest],
    "previous_cancellations": [previous_cancellations],
    "previous_bookings_not_canceled": [previous_bookings_not_canceled],
    "reserved_room_type": [reserved_room_type],
    "assigned_room_type": [assigned_room_type],
    "booking_changes": [booking_changes],
    "deposit_type": [deposit_type],
    "customer_type": [customer_type],
    "adr": [adr],
    "required_car_parking_spaces": [required_car_parking_spaces],
    "total_of_special_requests": [total_of_special_requests]
})

sample = pd.get_dummies(sample)

sample = sample.reindex(
    columns=columns,
    fill_value=0
)

sample = scaler.transform(sample)


if st.button("Predict Cancellation"):

    prediction = model.predict(sample)

    if prediction[0] == 1:
        st.error("❌ Prediction: This booking is likely to be Cancelled.")
        st.warning("The booking has a high probability of cancellation.")
    else:
        st.success("✅ Prediction: This booking is likely to be Confirmed.")

    probability = model.predict_proba(sample)

    confidence = probability.max() * 100

    st.write(f"### Confidence: {confidence:.2f}%")
    st.progress(int(confidence))
    st.markdown("---")
    st.caption("2nd Model made using logistic regression!")
    st.markdown("---")
st.markdown(
    "Developed by **Pranav Rane** | Machine Learning Project | Streamlit"
)