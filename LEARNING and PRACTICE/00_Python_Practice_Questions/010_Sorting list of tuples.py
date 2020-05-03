/*
Sorting list of tuples

You are provided with a list of tuples having three elements, name, age and salary. You are required to arrange the tuples in order of any of the three elements. The variable (name/age/salary) has to be decided by the second input, which is an integer (1 : name, 2 : Age, 3 : Salary). Make sure that the ordering should be ascending.



Example:

   Input 1 : [('Ram', 23 , 3000) , ('Mohan' , 22 , 4000 ) , ( 'Suresh' , 19 , 8000)]

             2

   Output 1:[ ( 'Suresh' , 19 , 8000) , ('Mohan' , 22 , 4000 ) ,('Ram', 23 , 3000)]



*/


import ast,sys

input_str = input()
input_list = ast.literal_eval(input_str)

sorting_choice = int(input())
 
custom_sorted_list = sorted(input_list, key = lambda entry: (-entry[sorting_choice - 1]))
print(custom_sorted_list)

