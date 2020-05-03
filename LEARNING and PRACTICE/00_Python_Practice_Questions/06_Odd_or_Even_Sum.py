/*

Odd or Even Sum
Given a positive integer as input, you have to find whether the sum of its digits is odd or even.

The input will have a positive integer and the output should say "odd" if the sum of its digits is odd and "even" if the sum of its digits is even.

Sample Input:
1234567
Sample Output:
even

*/

n=int(input())

# n actual no
r = 0 # reminder
m = n # remaining No
sum = 0 

while(m>0):
    r = m%10
    m = m//10
    sum = sum + r
    
if sum % 2 == 0:
    print("even")
else:
    print("odd")
