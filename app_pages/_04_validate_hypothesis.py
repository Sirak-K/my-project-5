import streamlit as st
from src.snsplot import plot_histogram_and_boxplot
from src.data_management import load_house_price_data


def _04_validate_hypothesis_body():

    df = load_house_price_data()

    st.write("### Project Hypothesis and Validation")

    # conclusions taken from DataExploration notebook
    st.success(
        f"* We suspect that there is a few very high sale prices."
        f" The combined boxplot/histogram below confirms that:"
        f" The histogram extends far to the right."
        f" It has a long tail.  \n"
        f"* The price values well beyond the average range are called outliers"
        f" and are shown as dots to the right of the box in the boxplot. "
        f" They correspond to sale prices above $466075"
    )

    # The Box-plot/histogram of the target variable "SalePrice"
    # - from DataExploration notebook
    df2 = df.filter(['SalePrice'])
    plot_histogram_and_boxplot(df2)

    st.info(
        f"* The models we have created may not accurately predict sale prices"
        f" above $400000 (see scatterplots on the ML Regressor Model page). \n"
        f"* This could be connected to the outliers mentioned above" 
        f" (with sale prices above $466075)."
        f"Initial steps were taken to improve the model for predicting"
        f" higher prices: The sale price was transformed to make "
        f" its distribution more symmetrical but more work is needed: "
        f" For each transformation tried, include it in the ML model" 
        f" and evaluate the new model."
    )
