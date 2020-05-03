/*

BMI Groups
Description
Create another feature based called BMI_group which groups people based on their BMI. The groups should be as follows:
Underweight: BMI is less than 18.5.
Normal: BMI is 18.5 to 24.9.
Overweight: BMI is 25 to 29.9.
Obese: BMI is 30 or more.
The grouping is based on WHO standards.

The output should have first five rows of the resulting dataframe.

Execution Time Limit
Default.

*/

import pandas as pd 

def addBMILable(value):
    if value < 18.5:
        return "Underweight"
    elif value >= 18.5 and value <= 24.9:
        return "Normal"
    elif value >= 25 and value <= 29.9:
        return "Overweight"
    else:
        return "Obese"


df=pd.read_csv("https://media-doselect.s3.amazonaws.com/generic/OzvzVqK4pgg4x7qEadoZMRyVR/insurance.csv")
# print(df.head())

df["BMI_group"] = df["bmi"].apply(addBMILable)
print(df.head())





