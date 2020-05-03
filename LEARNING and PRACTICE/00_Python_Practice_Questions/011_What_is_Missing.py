/*
What's Missing?

For a given list of integers in increasing order from n to m with no duplicates and common difference between two consecutive numbers being 1 except where the number is missing  with total  m-n integers in list, find out the missing number.

Sample input : [ 8,9,10,12}
Sample Output : 11

*/


# Import the relevant libraries
import ast,sys

# Read the input list

input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

list_sum = sum(input_list)

min_no = min(input_list)
max_no = max(input_list)

sum = 0
for i in range(min_no, max_no+1):
    sum = sum + i
    
print(sum -list_sum)

# Write your code here

