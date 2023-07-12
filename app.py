import streamlit as st
from app_pages.multi_page import MultiPage

# Load Scripts: Pages
from app_pages._01_project_summary import _01_project_summary_body
from app_pages._02_project_findings import _02_project_findings_body
from app_pages._03_target_prediction import _03_target_prediction_body
from app_pages._04_validate_hypothesis import _04_validate_hypothesis_body
from app_pages._05_pipeline_and_model import _05_pipeline_and_model_body

# Create an instance of the app
app = MultiPage(app_name="House Prices in Ames, Iowa")

# Add app pages using .add_page()
app.add_page("Quick Project Summary", _01_project_summary_body)
app.add_page("House Price Study", _02_project_findings_body)
app.add_page("Predict House Price", _03_target_prediction_body)
app.add_page("Project Hypothesis", _04_validate_hypothesis_body)
app.add_page("ML Regressor Model", _05_pipeline_and_model_body)

app.run()  # Run the app
