/*

Prime Numbers
Description
Determine whether a positive integer n is a prime number or not. Assume n>1.
Display “number entered is prime” if n is prime, otherwise display “number entered is not prime”.
Sample Input:
7
Sample Output:
number entered is prime
Execution Time Limit
Default.

*/

def checkPrime(n):
    if(n == 2):
        print("number entered is prime")
        return

    divCount = 0    
    for i in range(1, n):
        if n%i == 0:
            divCount = divCount + 1
            
    
    if divCount > 2:
        print("number entered is not prime")
    else:
        print("number entered is prime")
    
    
    
n=int(input())
#write your code here
checkPrime(n)



