/*

Cleaning columns
Description
For the given dataframe, you have to clean the "Installs" column and print its correlation with other numeric columns of the dataframe.(print df.corr())
You have to do the following:
1. Remove characters like ',' from the number of installs.
2. Delete rows where the Installs column has irrelevant strings like 'Free'
3. Convert the column to int type
You can access the dataframe using the following URL in your Jupyter notebook:
https://media-doselect.s3.amazonaws.com/generic/8NMooe4G0ENEe8z9q5ZvaZA7/googleplaystore.csv 
Note: You should try this problem on your own Jupyter notebook before submitting. Do not clean any column other than "Installs".
Sample Output:
            Rating  Installs
Rating    1.000000  0.051355
Installs  0.051355  1.000000
Execution Time Limit
Default.


*/


import pandas as pd 
df=pd.read_csv("https://media-doselect.s3.amazonaws.com/generic/8NMooe4G0ENEe8z9q5ZvaZA7/googleplaystore.csv")
#add your cleaning code here
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)
# 1. Remove characters like ',' from the number of installs.
df["Installs"] = df["Installs"].astype(str).apply(lambda x: x.replace(",",""))
df["Installs"] = df["Installs"].astype(str).apply(lambda x: x.replace("+",""))
# print(df["Installs"])

# 2. Delete rows where the Installs column has irrelevant strings like 'Free'
df.drop(df[df.Installs == "Free"].index, inplace = True)

# 3. Convert the column to int type
df["Installs"] = df["Installs"].astype(int)

print(df.corr())
