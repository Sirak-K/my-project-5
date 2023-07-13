import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load house price data


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_house_price_data():
    df = pd.read_csv("outputs/datasets/collection/house_prices_records.csv")
    return df

# Load correlation coefficients - from DataExploration notebook


def load_corr():
    df = pd.read_csv("outputs/eda_study/corr_df_rev.csv")
    return df

# Load pkl file


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)
