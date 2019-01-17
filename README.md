# Modeling Housing Prices in Ames, Iowa
_Author: Hunter Henninger (SF)_ 

## Problem Statement
The goal of this project is to formulate a regression model based on the Ames Housing Dataset. Through a process of data cleaning, preprocessing, and model tuning, this study aims to make accurate predictions of the selling price of a house. Analysis of appropriate metrics will provide insight into the quality of the predictive model. In doing this, home owners and real estate investors gain a better understanding of the most significant factors affecting the prices at sale. This study will provide clear recommendations and ways of boosting the value of homes to achieve maximum selling prices.

## Executive Summary
This study will incorporate the Ames Housing Dataset sourced by Ames, Iowa's Accessor Office to create the model. The portion of this dataset that is cleaned, preprocessed, and modeled consists of 2051 houses in Ames, Iowa between the years 2006 and 2010. An analysis of 80 features for homes including both numerical and categorical data seeks to use these features to predict the selling price of each house. The accuracy of these predictions can be interpreted by home owners and real estate investors as a way to boost the price of a house at sale. 

The study begins with a data cleaning process to handle missing data and outliers. A cleaned dataset is then preprocessed and visualized using various plots to determine basic trends between each feature and sale prices. Once a list of "interesting" features is selected, a multiple linear regression is evaluated. After a series of model tuning steps including a regularization penalty, coefficents are pulled out for practical interpretation. This predictive model proves that there are realistic methods for improving the value of home in Ames, Iowa.


## Contents:
- [01_Data Cleaning](./01_Data_Cleaning.ipynb)
- [02_Preprocessing and EDA](./02_Preprocessing_and_EDA.ipynb)
- [03_Model Benchmarks](./03_Model_Benchmarks.ipynb)
- [04_Model Tuning and Predictions](./04_Model_Tuning_and_Predictions.ipynb)
- [05_Model Insights](./05_Model_Insights.ipynb)

## Data Dictionary
Link to Data Description below:

[data description](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt)

## Conclusions and Recommendations

#### Key Remarks:
This model is conclusive in that it provides statistically significant evidence of predictive power regarding house prices at sale in Ames, Iowa. Therefore, with new data, this model can predict the price at sale of a house in Ames, Iowa with 90% more accuracy than simply calculating the average. This study identified the most important factors affecting the selling price of a house as exterior quality, kitchen quality, square footage, and number of full bathrooms. Although this model performs relatively well, the results are restricted by a limited dataset focused on only one city. An interesting study to extend this experiment would be to collect data on the exact same list of features for a different city in the United States and apply this model. Comparing the R-squared value and coefficients would lead to profound insight into a more general outlook of the selling price of a house. 

#### Recommendationms
The features that appeared most frequently as strong predictors were above ground square feet, the overall quality, the exterior quality, the square footage of the basement, the kitchen quality, the number of full bathrooms, and the year the house was built. 
<br><br>
For homeowners or real estate investors looking to maximize the selling price of a home: 
- increase square footage (basement, garage)
- improve the quality of the outside of the house
- improve the quality of the kitchen
- add full bathrooms