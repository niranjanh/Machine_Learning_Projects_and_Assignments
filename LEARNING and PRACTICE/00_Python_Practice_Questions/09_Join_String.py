/*

Join String
Given a list of strings, join them using the delimiter  '-' 

Sample Input : ['Accountability', 'and', 'Ownership']

Sample Output : Accountability-and-Ownership


*/

# Import the relevant libraries

import ast,sys

# Read the input list

input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

string_op = "-".join(input_list)
print(string_op)
# Write your code here



