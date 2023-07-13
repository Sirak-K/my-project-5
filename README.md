

# Table of Contents

-   [Dataset Content](https://chat.openai.com/c/3131c18c-31c3-48b7-b1e8-5b580b84ea80#dataset-content)
-   [Project Terminology](https://chat.openai.com/c/3131c18c-31c3-48b7-b1e8-5b580b84ea80#project-terminology)
-   [Business Requirements](https://chat.openai.com/c/3131c18c-31c3-48b7-b1e8-5b580b84ea80#business-requirements)
-   [Hypothesis and How to Validate?](https://chat.openai.com/c/3131c18c-31c3-48b7-b1e8-5b580b84ea80#hypothesis-and-how-to-validate)
-   [ML Business Case](https://chat.openai.com/c/3131c18c-31c3-48b7-b1e8-5b580b84ea80#ml-business-case)
-   [Dashboard Design (Streamlit App User Interface)](https://chat.openai.com/c/3131c18c-31c3-48b7-b1e8-5b580b84ea80#dashboard-design-streamlit-app-user-interface)
-   [Unfixed Bugs](https://chat.openai.com/c/3131c18c-31c3-48b7-b1e8-5b580b84ea80#unfixed-bugs)
-   [Deployment](https://chat.openai.com/c/3131c18c-31c3-48b7-b1e8-5b580b84ea80#deployment)
-   [Main Data Analysis and Machine Learning Libraries](https://chat.openai.com/c/3131c18c-31c3-48b7-b1e8-5b580b84ea80#main-data-analysis-and-machine-learning-libraries)
-   [Credits](https://chat.openai.com/c/3131c18c-31c3-48b7-b1e8-5b580b84ea80#credits)

# Project Terminology
## Correlation Analysis
#### The examination of the relationship or association between variables, in this case, house attributes and sale prices.

## House Attributes
#### The characteristics or features of a house that can influence its value, such as the number of bedrooms, square footage, location, etc.

## House Prices
#### The monetary value or sale price of residential properties.

## Property Appraisal
#### The process of estimating the value of a property.

##  Sales Price
#### The amount at which a property is sold or offered for sale.



## Dataset Content

The dataset from Kaggle has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|



# Business Requirements
As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to help in maximizing the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that

-   1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualizations of the correlated variables against the sale price to show that.
-   2 - The client is interested to predict the house sales price from her 4 inherited houses, and any other house in Ames, Iowa.


## Hypothesis and Validation
- The distribution of sale prices exhibits a right-skewness, which can pose difficulties in accurately predicting higher sale prices. 
- In order to validate the project hypothesis regarding the distribution shape - a combined boxplot and histogram of the sale prices is plotted.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

### **Business Requirement 1: Correlation Study and Data Visualization** 
1.  The client desires to examine the house records data to gain insights into the variables' significance concerning the sale price.
2.  The client requests a heatmap displaying the Spearman correlation coefficients to facilitate the ordering of variables based on their importance in relation to the sale price.
3.  The client intends to visualize the correlation between the important variables and the sale price by plotting them together.

### **Business Requirement 2:  Target Prediction & Data Analysis with Machine Learning** 
1.  The client seeks to access the inherited house records data for easy identification of specific house attributes.
2.  The client wishes to employ an ML model to predict the prices of their four inherited houses located in Ames, Iowa.
3.  The client aims to utilize the ML model for predicting the price of any other house in Ames, Iowa.


## ML Business Case
**1. What are the business requirements?**
    - The client is interested in understanding the correlation between house attributes and sale prices through data visualizations.
    - The client wants to predict sale prices for their inherited houses and other houses in Ames, Iowa.

**2. Is there any business requirement that can be answered with conventional data analysis?**
    - Yes, conventional data analysis can be used to explore the correlation between house attributes and sale prices.

**3. Does the client need a dashboard or an API endpoint?**
    - The client specifically requires a dashboard.

**4. What does the client consider as a successful project outcome?**
    - The client expects a comprehensive study revealing the most relevant variables correlated to sale price.
    - The client desires the ability to accurately predict sale prices for the inherited houses and other houses in Ames, Iowa.

**5. Can you break down the project into Epics and User Stories?**
    - Epic: Information gathering and data collection.
    - Epic: Data visualization, cleaning, and preparation.
    - Epic: Model training, optimization, and validation.
    - Epic: Dashboard planning, designing, and development.
    - Epic: Dashboard deployment and release.

**6. Ethical or Privacy concerns?**
    - No, as the client has obtained a public dataset.

**7. Does the data suggest a particular model?**
    - The data implies the suitability of a regressor model with the sale price as the target variable.

**8. What are the model's inputs and intended outputs?**
    - The inputs for the model are house attribute information, and the intended output is the predicted sale price.

**9. What are the criteria for the performance goal of the predictions?**
    - The agreed performance goal is to achieve an R2 score of at least 0.75 on both the train and test sets.

**10. How will the client benefit?**
    - The client will be able to maximize the sales price for their inherited properties, making informed decisions based on the most influential variables correlated to sale price.

## Dashboard Design 

### Page 1: Project Summary
- Overview of the dataset
- Overview of the business requirements
### Page 2: Project Findings
- Explains the client's expectations
- Presents the most relevant features and their meanings
### Page 3: Target Prediction
- Presents the inherited houses' attributes, their predicted sale prices and the sum of all four houses
- Contains the interactive input widget for running predictive analysis of the target variable
### Page 4: Project Hypothesis
- Presents the distribution shape of the target variable
- Presents the range for outliers
- Presents the hypothesis for the limitations of the ML model

### Page 5: Model & Pipeline
- Pipeline Structure
- Model Performance Evaluation
- The two most important house attributes

## Unfixed Bugs
No bugs found.

## Deployment
### Heroku

## Main Data Analysis and Machine Learning Libraries

- **numpy**==1.18.5
  - Numerical computing library for efficient array operations.

- **pandas**==1.4.2
  - Data manipulation and analysis tool for structured data.

- **matplotlib**==3.3.1
  - Data visualization library for creating static, animated, and interactive plots.

- **seaborn**==0.11.0
  - Statistical data visualization library for creating informative and attractive graphics.

- **ydata-profiling**==4.3.1
  - Automated exploratory data analysis tool for generating data profiles.

- **streamlit**==1.0.0
  - Python framework for building interactive web applications for data science.

- **feature-engine**==1.0.2
  - Library for feature engineering tasks such as encoding, imputation, and scaling.

- **scikit-learn**==0.24.2
  - Machine learning library for classification, regression, and clustering tasks.

- **plotly**==4.12.0
  - Interactive data visualization library for creating interactive plots and dashboards.

- **ppscore**==1.2.0
  - Library for calculating predictive power scores to measure feature importance.

- **xgboost**==1.21
  - Gradient boosting library for optimized and high-performance machine learning models.


## Credits 
### Content 
#### Coding Resources:
The work for this project was inspired by the content in Code Institute's course modules:
- Scikit-Learn
- Machine Learning Algorithms
- ML Walkthrough Projects 

### Media
#### [Icons for Dashboard - Twemoji](https://twitter.github.io/twemoji/2/test/preview.html)

## Acknowledgements
I want to express my gratitude towards my mentor for helping me plan my project.
