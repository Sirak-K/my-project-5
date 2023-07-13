import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.evaluate import regression_performance
from src.evaluate import regression_evaluation
from src.evaluate import regression_evaluation_plots


def _05_pipeline_and_model_body():

    # Load house price pipeline files
    pipeline = load_pkl_file(
        f"outputs/target_prediction/best_regressor_pipeline.pkl")
    house_price_feat_importance = plt.imread(
        f"outputs/target_prediction/features_importance.png")
    X_train = pd.read_csv(f"outputs/target_prediction/X_train.csv")
    X_test = pd.read_csv(f"outputs/target_prediction/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/target_prediction/y_train.csv").squeeze()
    y_test = pd.read_csv(
        f"outputs/target_prediction/y_test.csv").squeeze()

    st.write("### ML house price pipeline")

    # Summary of model performance
    st.info(
        f"* We agreed with the client on an R2 score of at least 0.75"
        f" on both train and test set.  \n"
        f"* The pipeline achieves 0.86 and 0.80 on the train set and test set" 
        f" respectively  \n"
    )
    st.write("---")

    # Present pipeline steps
    st.write("* **ML pipeline to predict house sale price**")
    st.write(pipeline)
    st.write("---")

    # Show the best features and their importance for the ML model
    st.write("* **The features of the model was trained by importance**")
    st.info("We see that the most important variable for predicting"
            " the sale price is 'OverallQual'")
    st.write(X_train.columns.to_list())
    st.image(house_price_feat_importance)
    st.write("---")

    # Evaluate performance on train and test sets
    regression_performance(X_train=X_train, y_train=y_train,
                           X_test=X_test, y_test=y_test, pipeline=pipeline)

    st.write("---")

    # Plot predicted versus actual sale price for train and test sets
    st.write("* **Predicted versus actual sale price scatterplot**")
    st.info("* For prices below $400000, the data points follow the "
            "red line where the predicted price equals actual price.  \n"
            "* For higher prices, our model may not accurately predict prices."
            " On the scatterplot showing the predictions on the train set"
            " (left plot below), the prices above $400000 are underestimated"
            " (the data points are below the red line)"
            )
    regression_evaluation_plots(X_train=X_train, y_train=y_train,
                                X_test=X_test, y_test=y_test,
                                pipeline=pipeline, alpha_scatter=0.5
                                )
