/*
Contiguous list
Given a list as input, your task is to check if the list is strictly increasing. i.e. the numbers in the list should be in an increasing order. Hence, a number at a lower index should always be smaller than a number at a higher index.
Assume that the list will only have positive integers.
Print "yes" if the list is in strictly increasing order and print "no" if the list is not strictly increasing. 

Sample Input:
[1,4,300,400,900]
Sample Output:
yes
*/

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

incerasing = True
for i in range(1, len(input_list)):
    if i < len(input_list):
        if incerasing and input_list[i-1] < input_list[i]:
            incerasing = True
        else:
            incerasing = False
            break
    
if incerasing:
    print("yes")
else:
    print("no")
