/*

Two series
Description
Given two pandas series, find the position of elements in series2 in series1.
You can assume that all elements in series2 will be present in series1.
The input will contain two lines with series1 and series2 respectively.
The output should be a list of indexes indicating elements of series2 in series 1.
Note: In the output list, the indexes should be in ascending order.
Sample Input:
[1,2,3,4,5,6,7]
[1,3,7]
Sample Output:
[0,2,6]

Execution Time Limit
Default.


*/


import ast,sys
import pandas as pd
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
series1=pd.Series(input_list[0])
series2=pd.Series(input_list[1])

# print(series2[series2 == 1].index[0])
out_list= series2.apply(lambda x: series1[series1 == x].index[0])

print(list(map(int,out_list)))#do not alter this step, list must be int type for evaluation purposes
