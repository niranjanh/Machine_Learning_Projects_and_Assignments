#Flatten a list
#Description
#Given a nested list, write python code to flatten the list.
#Note: The input list will strictly have 2 levels, i.e. the list will be of the form [[1,2],[3,4]]. Inputs like [1,[2,3]] and [[1,[2,3],4],5] #are not applicable.

#For example: If the input list is :
#[[1,2,3],[4,5],[6,7,8,9]]
#Then the output should be:
#[1,2,3,4,5,6,7,8,9]


import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

l = []

for i, item in enumerate(input_list):
    l = l + item
    
print(l)
