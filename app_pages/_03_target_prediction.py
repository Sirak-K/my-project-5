import streamlit as st
import numpy as np
import pandas as pd
from src.data_management import load_house_price_data, load_pkl_file


def _03_target_prediction_body():

    # Load files needed for predicting house prices

    pipeline = load_pkl_file(
        f"outputs/target_prediction/best_regressor_pipeline.pkl")
    best_features = (pd.read_csv(f"outputs/target_prediction/X_train.csv")
                     .columns
                     .to_list()
                     )

    # Load inherited houses data
    df = pd.read_csv(
        "inputs/datasets/raw/house-price-20211124T154130Z-001/"
        "house-price/inherited_houses.csv"
    )

    # Predict prices of inherited houses with the ML pipeline
    #  - from TargetPrediction notebook
    st.write("### House sale prices from client's inherited houses")
    st.write(
        f"* The table below shows the four inherited houses profile"
    )
    st.write(df.head())
    df = df.filter(best_features)
    house_price_prediction = pipeline.predict(df).round(0)
    df['Predicted House Sale Price'] = house_price_prediction
    st.write(
        f"* The table below shows the predicted sale prices for"
        f" the four houses, together with the house features"
        f" used in the prediction,"
        f" which are the two most important variables we saw"
        f" in the House Price Study page:"
        f" 'Overall Quality' and 'Above Ground Living Area Square Feet'."
    )
    st.write(df.head())

    # Calculate the sum of inherited houses predicted prices
    sum = df['Predicted House Sale Price'].sum()
    st.write(
        f"* The sum of the predicted sale prices for the four houses is:"
        f"&nbsp; &nbsp; &nbsp;{sum}  \n"
    )

    st.write("---")

    # Predict price of any other house in Ames, Iowa
    st.write("### Predict house sale prices in Ames, Iowa  \n")
    st.write("* Only the two house attributes"
             " 'Above Ground Living Area Square Feet' and 'Overall Quality' "
             " are needed for the ML model to predict the price.")
    st.warning("* The model has limitations: For example the maximum"
               "'Above Ground Living Area Square Feet'"
               " in the train set is 5642 square feet and one should "
               " not expect the model to generalize to larger areas."
               )
    # Create interactive input fields for live data
    X_live = DrawInputsWidgets()
    # Predict on live data
    if st.button("Run Predictive Analysis"):
        house_price_prediction = pipeline.predict(
            X_live.filter(best_features)).round(0)
        st.write(
            f"* The predicted sale price for the house is:"
            f" &nbsp; &nbsp; &nbsp;{house_price_prediction[0]}  \n"
        )


# Create input fields
def DrawInputsWidgets():

    # Load dataset
    df = load_house_price_data()
    percentageMin, percentageMax = 0.5, 1.0

    # Create input widgets only for two features
    col1, col2 = st.columns(2)

    # We are using these features to feed the ML pipeline

    # Create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # From here on we draw the widget based on the variable type 
    # (numerical or categorical) and set initial values
    with col1:
        feature = 'GrLivArea'
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col2:
        feature = "OverallQual"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].sort_values(ascending=True).unique()
        )
    X_live[feature] = st_widget

    return X_live
