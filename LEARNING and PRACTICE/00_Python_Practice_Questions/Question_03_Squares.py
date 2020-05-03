#Squares
#Description
#Given a list of positive integers, you have to find numbers divisible by 3 and replace them with their squares. 
#For example, consider the list below:
#Input: [1,2,3,4,5,6]
#The output for the above list would be: [1,2,9,4,5,36]. Because 3 and 6 were divisible by 3, these numbers were replaced with their squares.


import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

for i, item in enumerate(input_list):
    if item % 3 == 0:
        input_list[i] = item ** 2
        
print(input_list)
