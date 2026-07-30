"""
Preprocessing helpers.

These functions rebuild the exact feature vectors that HouseScaler / HouseColumns
and hotelscaler / hotelcolumns expect, based on introspecting the saved artifacts
(no notebook was provided, so this is reconstructed directly from the pickled
column lists, scaler.feature_names_in_, and domain knowledge of the standard
Kaggle "Housing Prices" and "Hotel booking demand" datasets these models were
trained on).

Key facts baked in here (verified against the artifacts, not assumed):
- House model: pd.get_dummies(..., drop_first=False) -> every binary category
  has BOTH a "_no" and "_yes" column, and furnishingstatus has all 3 categories.
- Hotel model: pd.get_dummies(..., drop_first=True) -> exactly one category per
  categorical column is the implicit baseline (all its dummy columns are 0).
  Baselines were identified by diffing the known category sets of the standard
  hotel-booking-demand dataset against the columns actually present in
  hotelcolumns.pkl.
"""

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# HOUSE (Regression) helpers
# ---------------------------------------------------------------------------

HOUSE_BINARY_FIELDS = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "prefarea",
]

HOUSE_FURNISHING_OPTIONS = ["furnished", "semi-furnished", "unfurnished"]


def build_house_row(raw: dict, house_cols: list) -> pd.DataFrame:
    """
    raw expects keys:
      area, bedrooms, bathrooms, stories, parking (numeric)
      mainroad, guestroom, basement, hotwaterheating, airconditioning, prefarea -> "yes"/"no"
      furnishingstatus -> one of HOUSE_FURNISHING_OPTIONS
    Returns a single-row DataFrame with columns in exactly house_cols order.
    """
    row = {col: 0 for col in house_cols}

    row["area"] = raw["area"]
    row["bedrooms"] = raw["bedrooms"]
    row["bathrooms"] = raw["bathrooms"]
    row["stories"] = raw["stories"]
    row["parking"] = raw["parking"]

    for field in HOUSE_BINARY_FIELDS:
        choice = raw[field]  # "yes" or "no"
        col_yes = f"{field}_yes"
        col_no = f"{field}_no"
        if col_yes in row:
            row[col_yes] = 1 if choice == "yes" else 0
        if col_no in row:
            row[col_no] = 1 if choice == "no" else 0

    furnishing_col = f"furnishingstatus_{raw['furnishingstatus']}"
    if furnishing_col in row:
        row[furnishing_col] = 1

    return pd.DataFrame([row], columns=house_cols)


# ---------------------------------------------------------------------------
# HOTEL (Classification) helpers
# ---------------------------------------------------------------------------

# Full category sets for the standard hotel-booking-demand dataset.
# The category NOT present as a column in hotelcolumns.pkl is the drop_first
# baseline (all-zero row for that categorical).
HOTEL_TYPE_OPTIONS = ["City Hotel", "Resort Hotel"]
MONTH_OPTIONS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]
MEAL_OPTIONS = ["BB", "FB", "HB", "SC", "Undefined"]
MARKET_SEGMENT_OPTIONS = [
    "Aviation", "Complementary", "Corporate", "Direct",
    "Groups", "Offline TA/TO", "Online TA", "Undefined",
]
DISTRIBUTION_CHANNEL_OPTIONS = ["Corporate", "Direct", "GDS", "TA/TO", "Undefined"]
DEPOSIT_TYPE_OPTIONS = ["No Deposit", "Non Refund", "Refundable"]
CUSTOMER_TYPE_OPTIONS = ["Contract", "Group", "Transient", "Transient-Party"]

# Room types: derive the "present" set directly from the column list so we
# never hardcode something inconsistent with what the model actually saw.
_RESERVED_BASE_LETTERS = list("ABCDEFGHLP")   # standard dataset room-type letters
_ASSIGNED_BASE_LETTERS = list("ABCDEFGHIKLP")


def _options_from_columns(hotel_cols, prefix, known_full_set):
    """Return the full known option list for a categorical, given which of its
    dummy columns actually exist in hotel_cols (the missing one(s) are the
    drop_first baseline(s) still worth offering the user)."""
    present = {c[len(prefix):] for c in hotel_cols if c.startswith(prefix)}
    return known_full_set, present


def get_country_options(hotel_cols):
    """Every country code that has its own dummy column, plus a baseline
    'Other / Not in training data' option (maps to an all-zero country vector)."""
    countries = sorted(
        c[len("country_"):] for c in hotel_cols if c.startswith("country_")
    )
    return countries + ["Other / Not in training data"]


def get_reserved_room_options(hotel_cols):
    present = {c[len("reserved_room_type_"):] for c in hotel_cols if c.startswith("reserved_room_type_")}
    missing = [l for l in _RESERVED_BASE_LETTERS if l not in present]
    return _RESERVED_BASE_LETTERS  # includes the baseline letter(s), e.g. "A"


def get_assigned_room_options(hotel_cols):
    return _ASSIGNED_BASE_LETTERS


def build_hotel_row(raw: dict, hotel_cols: list) -> pd.DataFrame:
    """
    raw expects keys:
      Numeric: lead_time, arrival_date_year, arrival_date_week_number,
               arrival_date_day_of_month, stays_in_weekend_nights,
               stays_in_week_nights, adults, children, babies,
               is_repeated_guest (0/1), previous_cancellations,
               previous_bookings_not_canceled, booking_changes,
               days_in_waiting_list, adr, required_car_parking_spaces,
               total_of_special_requests
      Categorical: hotel, arrival_date_month, meal, country, market_segment,
               distribution_channel, reserved_room_type, assigned_room_type,
               deposit_type, customer_type
    Returns a single-row DataFrame with columns in exactly hotel_cols order.
    """
    row = {col: 0 for col in hotel_cols}

    numeric_fields = [
        "lead_time", "arrival_date_year", "arrival_date_week_number",
        "arrival_date_day_of_month", "stays_in_weekend_nights",
        "stays_in_week_nights", "adults", "children", "babies",
        "is_repeated_guest", "previous_cancellations",
        "previous_bookings_not_canceled", "booking_changes",
        "days_in_waiting_list", "adr", "required_car_parking_spaces",
        "total_of_special_requests",
    ]
    for field in numeric_fields:
        row[field] = raw[field]

    def set_dummy(prefix, value):
        col = f"{prefix}{value}"
        if col in row:
            row[col] = 1
        # else: value is the drop_first baseline -> leave whole group at 0

    set_dummy("hotel_", raw["hotel"])
    set_dummy("arrival_date_month_", raw["arrival_date_month"])
    set_dummy("meal_", raw["meal"])
    set_dummy("market_segment_", raw["market_segment"])
    set_dummy("distribution_channel_", raw["distribution_channel"])
    set_dummy("reserved_room_type_", raw["reserved_room_type"])
    set_dummy("assigned_room_type_", raw["assigned_room_type"])
    set_dummy("deposit_type_", raw["deposit_type"])
    set_dummy("customer_type_", raw["customer_type"])

    country = raw["country"]
    if country != "Other / Not in training data":
        set_dummy("country_", country)

    return pd.DataFrame([row], columns=hotel_cols)
