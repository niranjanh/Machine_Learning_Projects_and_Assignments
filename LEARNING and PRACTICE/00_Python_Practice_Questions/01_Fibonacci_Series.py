/*

Fibonacci Series
Description
Compute and display Fibonacci series upto n terms where n is a positive integer entered by the user.
You can go here to read about Fibonacci series.
Sample Input:
5
Sample Output:
0
1
1
2
3
Execution Time Limit
Default.

*/


def printFib(n):
    n1 = 0
    n2 = 1
    sum = 0
    
    if n == 0:
        print(n1)
        return
    elif n == 1:
        print(n1)
        return
    
    print(n1)
    print(n2)
    
    n = n-2
    
    while(n):
        sum = n1 + n2
        print(sum)
        n1 = n2
        n2 = sum
        n = n - 1

n=int(input())
#write your code here
printFib(n)


