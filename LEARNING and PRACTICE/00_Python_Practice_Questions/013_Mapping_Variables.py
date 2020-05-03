/*

Mapping Variables


Description
You're given two lists, the first of which contains the name of some people and the second contains their corresponding 'response'. These lists have been converted to a dataframe. 
Now, the values that the 'response' variable can take are ‘Yes’, ‘No’, and ‘Maybe’. Write a code to map these variables to the values ‘1.0’, ‘0.0’, and ‘0.5’.

Note: It also might happen the the first letter of the three responses are not in uppercase, i.e. you might also have the values 'yes', 'no', and 'maybe' in the dataframe. So make sure you handle that in your code.

Example:
Input 1:
['Reetesh', 'Shruti', 'Kaustubh', 'Vikas', 'Mahima', 'Akshay']
['No', 'Maybe', 'yes', 'Yes', 'maybe', 'Yes']
Output 1:
﻿
﻿
Execution Time Limit


*/



# Reading the input
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
# Storing the names in a variable 'name'
name = input_list[0]
# Storing the responses in a variable 'repsonse'
response = input_list[1]

# Importing pandas and converting the read lists to a dataframe. You can print
# the dataframe and run the code to see what it will look like
import pandas as pd 
df = pd.DataFrame({'Name': name,'Response': response})

df['Response'] = df['Response'].apply(lambda x: 1.0 if x == "Yes" or x == "yes" else 0.0 if x == "No" or x == "no" else 0.5)

# Print the final DataFrame
# print(df)
print(df)
