/*


Smoking kills
Description
As everyone knows, smoking is a major cause of bad health. Here, try to find if smoking is affecting health of people.
Print the correlation value of "smoker" columns with "bmi", "age"  and "charges" columns in three lines respectively.

Note: You should round off all three values till four decimal places using the round() function.
Execution Time Limit
Default.


*/

import pandas as pd 
df=pd.read_csv("https://media-doselect.s3.amazonaws.com/generic/B5yO4wkEbQk4dVGn8140yV1bx/insurance_encoded.csv")
cor = df.corr()

print('{:.4f}'.format(round(cor["smoker"]["bmi"], 4)))
print('{:.4f}'.format(round(cor["smoker"]["age"], 4)))
print('{:.4f}'.format(round(cor["smoker"]["charges"], 4)))

