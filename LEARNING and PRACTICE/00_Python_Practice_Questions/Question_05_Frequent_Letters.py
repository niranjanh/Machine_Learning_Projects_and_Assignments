#Frequent Letters
#Description
#Given a string, you have to find the first n most frequent characters in it.

#You have to print these n letters in alphabetically sorted order.

#The input will contain two lines, the first line will contain a string and the second line will contain the letter n.

#The output should be a list of n most frequent letters in alphabetically sorted order.

#Note: If there are two letters with the same frequency, then the alphabetically preceding alphabet should be picked first. (For example, in #"aabbccc", if n=2, then output list would have c and a.)

#Sample Input:

#ddddaacccb

#3

#Sample Output:

#['a', 'c', 'd']


#In the above example, the order of frequencies is : d>c>a>b

#Here, d,c and a are three most frequent characters which are displayed in alphabetically sorted order.


string=input()
n=int(input())
#write your code here
d = {}

for char in string:
    value = d.get(char, 0)
    d[char] = value + 1

v_dict = {}
for k,v in d.items():
    if v_dict.get(v) and ord(v_dict.get(v)) < ord(k):
        k = v_dict.get(v)
    v_dict[v] = k
    
value_order = sorted(v_dict, reverse = True)

result = []
for i in range(n):
    result.append(v_dict.get(value_order[i]))

result = sorted(result)
print(result)
