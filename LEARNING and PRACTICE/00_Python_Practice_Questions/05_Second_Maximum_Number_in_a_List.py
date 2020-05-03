/*

Second Maximum Number in a List
Description
Given a list of numbers, find the second largest number in the list. 

Note: There might be repeated numbers in the list. If there is only one number present in the list, return 'not present'.

Examples:
Input 1:
[7, 2, 0, 9, -1, 8]
Output 1:
8

Input 2:
[3, 1, 4, 4, 5, 5, 5, 0, 2, 2]
Output 2:
4

Input 2:
[6, 6, 6, 6, 6]
Output 2:
not present
Execution Time Limit
15 seconds

create

*/


# Read the input list
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

# Write your code here
l = sorted(input_list, reverse=True)

found = False

for i in range(1, len(l)):
    if l[i] == l[0]:
        continue
    else:
        found = True
        print(l[i])
        break

if not found:
    print("not present")


