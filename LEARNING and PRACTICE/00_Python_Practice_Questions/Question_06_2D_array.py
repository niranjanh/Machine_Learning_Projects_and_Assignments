#2D array

#Description

#Write Python code which takes 2 numbers x and y as input and generates a 2-dimensional numpy array where value in the i-th row and j-th column #of the array should be (i+j)/2.

#Note: i=0,1,...x-1 and j=0,1....,y-1

#The input will have two lines with x and y respectively.
#The output should be a 2D numpy array.

#Sample Input:
#3
#4

#Sample Output:

#[[0.  0.5 1.  1.5]
# [0.5 1.  1.5 2. ]
# [1.  1.5 2.  2.5]]




import numpy as np

def arrangeNumbers(arr, x, y):
    arr = [(i + j) /2 for i in range(x) for j in range(y) if x is not 0 and y is not 0]
    
    return arr

x=int(input())
y=int(input())
#write your code here

arr = np.full((x,y), 0)
arr[0, 0] = 0
arr[0, 1] = 1

arr = np.reshape(arrangeNumbers(arr, x, y), (x, y))
print(arr)

