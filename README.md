
### Table of Contents

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


# Project Terminology
## Correlation Analysis
#### The examination of the relationship or association between variables, in this case, house attributes and sale prices.
## Data Practitioner
#### A professional skilled in working with data, conducting analysis, and building models.
## House Attributes
#### The characteristics or features of a house that can influence its value, such as the number of bedrooms, square footage, location, etc.
## House Prices
#### The monetary value or sale price of residential properties.
## Property Appraisal
#### The process of estimating the value of a property.
##  Sales Price
#### The amount at which a property is sold or offered for sale.



## Business Requirements

* **Business Requirement 1:** 

* **Business Requirement 2:** 

## Hypothesis and how to validate?


## The rationale to map the business requirements to the Data Visualisations and ML tasks



## ML Business Case

### Predict:
#### Model: Regressor


## Dashboard Design 

### Page 1: Project Summary
### Page 2: House Sale Prices Study
### Page 3: Price Predictions
### Page 4: Project Hypothesis and Validation
### Page 5: Regressor Model & Pipeline Performance

## Unfixed Bugs

## Deployment
### Heroku

## Main Data Analysis and Machine Learning Libraries

## Credits 

### Content 

### Media
