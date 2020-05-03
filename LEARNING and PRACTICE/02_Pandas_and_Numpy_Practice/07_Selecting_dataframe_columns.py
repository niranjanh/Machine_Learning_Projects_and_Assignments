/*

Selecting dataframe columns
Description
Write a program to select all columns of a dataframe except the ones specified.
The input will contain a list of columns that you should skip.
You should print the first five rows of the dataframe as output where the columns are alphabetically sorted.

Sample Input:
['PassengerId', 'Pclass', 'Name', 'Sex','Embarked']
Sample Output:

    Age Cabin     Fare  Parch  SibSp   Ticket
0  34.5   NaN   7.8292      0      0   330911
1  47.0   NaN   7.0000      0      1   363272
2  62.0   NaN   9.6875      0      0   240276
3  27.0   NaN   8.6625      0      0   315154
4  22.0   NaN  12.2875      1      1  3101298

Execution Time Limit
Default.


*/

import pandas as pd
import ast,sys
df=pd.read_csv("https://media-doselect.s3.amazonaws.com/generic/X0kvr3wEYXRzONE5W37xWWYYA/test.csv")
input_str = sys.stdin.read()
to_omit = ast.literal_eval(input_str)
#write your code here
pd.set_option('display.max_columns', 500)

# df.sort_values(by = df.columns.tolist(), inplace = True, ascending=True, axis = 0)
df = df.reindex(columns=sorted(df.columns.tolist()))

df = df.drop(to_omit, axis = 1)

print(df.head())




