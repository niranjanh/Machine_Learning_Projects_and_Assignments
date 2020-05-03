#A weird sum
#Description
#Write a program that computes the value of n+nn+nnn+nnnn with a given digit as the value of n.
#For example, if n=9 , then you have to find the value of 9+99+999+9999.

n=int(input())

sum = 0

for i in range(1, 5):
    currentNo = 0
    for j in range(0, i):
        currentNo = currentNo + n * (10 ** j)
    
    sum = sum + currentNo
    
print(sum)


