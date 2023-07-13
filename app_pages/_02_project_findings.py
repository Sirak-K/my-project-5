import numpy as np
import streamlit as st
import sys
sys.path.append("./src")

from src.data_management import load_house_price_data
from src.data_management import load_corr
from src.data_management import load_pkl_file

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def _02_project_findings_body():

    # Load House Prices data
    # Load Correlation Coefficients
    # Load dictionary used for encoding
    # Define object variables
    df = load_house_price_data()
    df_corr = load_corr()
    dic = load_pkl_file('outputs/eda_study/dic.pkl')

    # Copied from DataExploration study notebook
    strong_correlation = ['OverallQual', 'GrLivArea', '2ndFlrSF',
                          'KitchenQual', 'YearBuilt', 'GarageArea',
                          'GarageFinish']
    moderate_correlation = ['GarageYrBlt', '1stFlrSF', 'TotalBsmtSF',
                            'YearRemodAdd', 'LotArea', 'LotFrontage',
                            'BsmtFinSF1']

    dtype_dict = {
        'OverallQual': 'object',
        'GrLivArea': 'numeric',
        '2ndFlrSF': 'numeric',
        'KitchenQual': 'object',
        'YearBuilt': 'numeric',
        'GarageArea': 'numeric',
        'GarageFinish': 'object',
        'GarageYrBlt': 'numeric',
        '1stFlrSF': 'numeric',
        'TotalBsmtSF': 'numeric',
        'YearRemodAdd': 'numeric',
        'LotArea': 'numeric',
        'LotFrontage': 'numeric',
        'BsmtFinSF1': 'numeric'
    }

    st.write("### House Sale Price study")
    st.info(
        f"* The client is interested in discovering how the house attributes"
        f"correlate with the sale price."
        f" Therefore, the client expects data visualizations of the correlated"
        f"variables against the sale price to show that.")

    # display housing data dataframe
    if st.checkbox("Inspect housing records dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    # Project Findings - Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to find "
        f"the most important variables for determining the sale price.  \n"
        f"The seven most important variables are (in order of importance):  \n"
        f"**{strong_correlation}**.  \n\n"
    )

    # Meaning of variables: From README file - "Dataset Content" section
    st.info(
        f"Meaning of variables:  \n"
        f"* **{strong_correlation[0]}**: Rates the overall material and finish"
        f" of the house.  \n"
        f"* **{strong_correlation[1]}**: Above grade (ground) living area"
        f"square feet. \n"
        f"* **{strong_correlation[2]}**: Second floor square feet. \n"
        f"* **{strong_correlation[3]}**: Kitchen quality. \n"
        f"* **{strong_correlation[4]}**: Original construction date. \n"
        f"* **{strong_correlation[5]}**: Size of garage in square feet. \n"
        f"* **{strong_correlation[6]}**: Rates the interior finish of the "
        f"garage. \n"
    )

    st.write(
        f"Seven other variables are still important but to a lesser degree:"
        f"They show moderate correlation with the sale price"
        f"(shown in order of importance):  \n"
        f"**{moderate_correlation}**.  \n"
    )

    # Meaning of variables: From README file - "Dataset Content" section
    st.info(
        f"Meaning of variables:  \n"
        f"* **{moderate_correlation[0]}**: Year garage was built.  \n"
        f"* **{moderate_correlation[1]}**: First Floor square feet. \n"
        f"* **{moderate_correlation[2]}**: Total square feet"
        f"of basement area. \n"
        f"* **{moderate_correlation[3]}**: Remodel date"
        f"(same as construction date if no remodeling or additions). \n"
        f"* **{moderate_correlation[4]}**: Lot size in square feet. \n"
        f"* **{moderate_correlation[5]}**: Linear feet of street"
        f"connected to property. \n"
        f"* **{moderate_correlation[6]}**: Type 1 finished square feet"
        f"of basement area. \n"
    )

    # Heatmap of correlation coefficients above 0.4
    if st.checkbox("Heatmap of the fourteen variables in order of importance."
                   "We see that the two most important variables"
                   " are 'Overall Quality' and 'Above Ground Living Area Sq."
                   "Feet'."):
        heatmap(df_corr)

    # Scatterplots of sale price against correlated variable
    if st.checkbox("Scatterplots for the seven most important attributes."
                   "They show how sale price increases with "
                   "the value of the attribute, e.g 'Overall Quality'."):

        st.success(
            f"* The plots below confirm the expectation that"
            f"the stronger the correlation the clearer the trend.  \n"
        )
        st.warning(
            f"* We also see that the spread in price increases with price.  \n"
        )
        st.write(f"* Plot Sale Price against attribute")
        scatterplot(df, dic, strong_correlation, dtype_dict)


# function created using code from "DataExploration" notebook - Heatmap section
def heatmap(df):
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    fig, axes = plt.subplots(figsize=(12, 5))
    annot_size = 8

    mask = np.zeros_like(df, dtype=np.bool)
    mask[abs(df) < 0.4] = True

    sns.heatmap(data=df, annot=True, xticklabels=True, yticklabels=True,
                mask=mask, cmap='viridis', annot_kws={"size": annot_size},
                ax=axes, linewidth=0.5)

    st.pyplot(fig)


# Function created using code from "DataExploration" notebook - Scatterplot
def scatterplot(df, dic, strong_correlation, dtype_dict):
    for col in strong_correlation:
        if df[col].dtype == 'object':
            df1 = df[df[col] != 'None']
            df2 = df1[df1[col].notnull()]
            df3[col] = df2[col].replace(dic[col])
        else:
            df1 = df[df[col] != 0]
            df3 = df1[df1[col].notnull()]
        if dtype_dict[col] == 'object':
            fig, axes = plt.subplots(figsize=(8, 5))
            sns.stripplot(data=df3, x=col, y='SalePrice')
            st.pyplot(fig)
        elif dtype_dict[col] == 'numeric':
            fig, axes = plt.subplots(figsize=(8, 5))
            sns.scatterplot(data=df3, x=col, y='SalePrice', alpha=0.5)
            st.pyplot(fig)
