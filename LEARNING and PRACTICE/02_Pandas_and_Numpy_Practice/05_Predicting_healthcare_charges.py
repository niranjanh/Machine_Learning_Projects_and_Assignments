/*

Predicting healthcare charges
Description
You saw that by using only the "smoker" variable, you can get an r-squared of 0.66 easily.
Now your task is to perform linear regression using the entire dataset. 
Note: All operations your performed in the questions 1-3 have already been performed on the dataset here. You can take any other measures to ensure a better outcome if you want.(for example: normalising or standardising any values or adding any other columns)
The dataset has been divided into train and test sets and both have been loaded in the coding console. 

You have to write the predictions in the file:
/code/output/predictions.csv

You have to add the predictions in a column titled "charges_predictions" in the test dataset.
Make sure you use the same column name otherwise your score won't be evaluated.

Your model's R-squared-adjusted will be evaluated on an unseen test dataset. The R-squared of your model should be greater than 0.72. You don't need to write any code for calculation of R-squared adjusted. It will automatically be evaluated on the unseen test set once you click Verify/Submit. 
Datasets
Training dataset
Execution Time Limit
Default.

*/

import numpy as np
import pandas as pd

# Read training data
train = pd.read_csv("https://media-doselect.s3.amazonaws.com/generic/QNdMORzykKkG4L3WQ17Xx53o3/insurance_training.csv")

# Read test data
test = pd.read_csv("https://media-doselect.s3.amazonaws.com/generic/Mq5p8YpQoz3KbWJRE4Mey1Yoq/insurance_test.csv")

# Linear regression
#import required libraries
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor


y_train = train.pop("charges")
X_train = train


# Add a constant to get an intercept
X_train_sm = sm.add_constant(X_train)

# Fit the resgression line using 'OLS'
lr = sm.OLS(y_train, X_train_sm).fit()
y_train_pred = lr.predict(X_train_sm)

# ON TEST DATASET
X_test = test

# Add a constant to X_test
X_test_sm = sm.add_constant(X_test)

# Predict the y values corresponding to X_test_sm
y_test_pred = lr.predict(X_test_sm)

# Write the output
test["predicted_charges"] = y_train_pred


# Write the output
test["predicted_charges"]=y_test_pred
test.to_csv("/code/output/predictions.csv")
