import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("bmw_model.pkl", "rb"))

st.title("BMW Price Category Predictor")

st.write("Enter vehicle details to predict the price category.")

# Numeric inputs
year = st.number_input("Year", min_value=2000, max_value=2024, step=1)
mileage = st.number_input("Mileage")
engineSize = st.number_input("Engine Size")

# Categorical inputs
fuelType = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "Hybrid", "Electric", "Other"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic", "Semi-Auto"]
)

model_name = st.selectbox(
    "BMW Model",
    ["1 Series", "2 Series", "3 Series", "4 Series", "5 Series", "X1", "X3", "X5"]
)

if st.button("Predict Price Category"):

    # Start dataframe with all features used during training
    model_features = model.feature_names_in_
    input_df = pd.DataFrame(columns=model_features)
    input_df.loc[0] = 0

    # Fill numeric features
    for col, val in {
        "year": year,
        "mileage": mileage,
        "engineSize": engineSize
    }.items():
        if col in input_df.columns:
            input_df[col] = val

    # Encode fuel type
    fuel_col = f"fuelType_{fuelType}"
    if fuel_col in input_df.columns:
        input_df[fuel_col] = 1

    # Encode transmission
    trans_col = f"transmission_{transmission}"
    if trans_col in input_df.columns:
        input_df[trans_col] = 1

    # Encode model
    model_col = f"model_{model_name}"
    if model_col in input_df.columns:
        input_df[model_col] = 1

    prediction = model.predict(input_df)

    st.success(f"Predicted Price Category: {prediction[0]}")