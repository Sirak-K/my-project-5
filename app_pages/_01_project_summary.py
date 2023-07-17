import streamlit as st


def _01_project_summary_body():

    st.write("### Project Summary")

    # Information from README file - "Dataset Content" section
    st.info(
        f"**Project Dataset**\n"
        f"* The dataset shows house sale prices in Ames, Iowa,"
        f" together with 23 features that could potentially "
        f" influence the price."
        f" Examples of features are first floor area, basement area,"
        f" wooddeck area, overall quality"
        f", kitchen quality, construction date and so on.\n\n")

    # Link to Dataset
    st.write(
        f"* View the dataset on "
        f"[Kaggle](https://www.kaggle.com/datasets/codeinstitute/"
        f"housing-prices-data).")

    # Link to README
    st.write(
        f"* For additional information, please see the project's "
        f"[README-file](https://github.com/Sirak-K/my-project-5).")

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in discovering "
        f"how the house attributes correlate with the sale price."
        f" Therefore, the client expects data visualizations of the correlated"
        f" variables against the sale price to show that.\n"
        f"* 2 - The client is interested to predict the house sale prices of"
        f"her 4 inherited houses."
    )
