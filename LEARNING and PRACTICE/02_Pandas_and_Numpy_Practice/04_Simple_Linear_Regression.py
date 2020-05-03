/*

Simple Linear Regression
Description
We have divided the dataset now into test and train sets.
Since you already saw that being a smoker and healthcare charges are highly correlated. Try to create a linear regression model using only the "smoker" variable as the independent variable and "charges" as dependent variable.
Note: All operations you performed in the previous questions have already been performed on the dataset here. You can take any other measures to ensure a better outcome if you want.
The dataset has been divided into train and test sets and both have been loaded in the coding console. 

You have to write the predictions in the file:
/code/output/predictions.csv

You have to add the predictions in a column titled "predicted_charges" in the test dataset.
Make sure you use the same column name otherwise your score won't be evaluated.

Your model's R-squared will be evaluated on an unseen test dataset. The R-squared of your model should be greater than 0.6. You don't need to write any code for calculation of Rsquared. It will automatically be evaluated on the unseen test set once you click Verify/Submit. 

Datasets
Training dataset
Execution Time Limit
Default.




*/



import numpy as np
import pandas as pd

# Read training data
train = pd.read_csv("https://media-doselect.s3.amazonaws.com/generic/72Boxj99702g8BwK5powGz1g0/insurance_training.csv")

# Read test data
test = pd.read_csv("https://media-doselect.s3.amazonaws.com/generic/gxVjwe1k3YEogYK23O8PPnXod/insurance_test.csv")

# Linear regression
#import required libraries
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor


X_train = train["smoker"]
y_train = train["charges"]
X_test = test["smoker"]

# Add a constant to get an intercept
X_train_sm = sm.add_constant(X_train)

# Fit the resgression line using 'OLS'
lr = sm.OLS(y_train, X_train_sm).fit()
y_train_pred = lr.predict(X_train_sm)

# ON TEST DATASET
# Add a constant to X_test
X_test_sm = sm.add_constant(X_test)

# Predict the y values corresponding to X_test_sm
y_test_pred = lr.predict(X_test_sm)

# Write the output
test["predicted_charges"] = y_train_pred


#THESE TWO LINES SHOULD NOT BE EDITED
test["predicted_charges"]=y_test_pred
test.to_csv("/code/output/predictions.csv")
