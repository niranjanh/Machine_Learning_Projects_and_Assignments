/*


Handling Categorical Variables
Description
Encode all categorical features such that they can be used in a regression model.
i.e.
sex, BMI_group, smoker and region should be labelled properly.

Note: Use the label encoder for all features. You can read more about it here.

The output should have first five rows of the resulting dataframe. 


Execution Time Limit
20 seconds

*/


import pandas as pd 
from sklearn.preprocessing import LabelEncoder
pd.set_option('display.max_columns', 500)
df=pd.read_csv("https://media-doselect.s3.amazonaws.com/generic/831JKKEkW7kqd5M4evNva9LyB/insurance_grouped.csv")
le = LabelEncoder()#use this encoder to encode values

vars = ["sex", "BMI_group", "smoker", "region"]

df["sex"] = le.fit_transform(df["sex"])
df["smoker"] = le.fit_transform(df["smoker"])
df["region"] = le.fit_transform(df["region"])

df["BMI_group"] = le.fit_transform(df["BMI_group"].astype(str))


# df[vars] = le.fit_transform(df[vars])
print(df.head())
