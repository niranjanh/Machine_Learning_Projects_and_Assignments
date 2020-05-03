/*

Finding common letters in string

You are provided two strings. You have to determine the common letters in the two strings. Make sure that the case difference is kept in mind. 'A' is not the same as 'a'. Also, note that the common letters are ordered in their alphabetical order.

Examples:
Input 1:
    S1  = 'Hello'
   S2  = 'World'
Output 1:
  The common letters are :
   l
  o

Input 2:
   S1 = 'abc'
   S2 = 'def'
Output 2:
  There are no common letters between them

*/


# Take the strings as input

s1=input()
s2=input()

d = dict()
for i in s1:
    d[i] = 1

count = 0
common_letters = []
for j in s2:
    value = d.get(j, 0)
    if value:
        common_letters.append(j)
        count = count + 1

if not count:
    print("There are no common letters between them")
else:
    print("The common letters are:")
    # print(sorted(common_letters))
    for v in sorted(common_letters):
        print(v)
    
# Write your code below



/*

SOLUTION 2:

# Take the strings as input

s1=input()
s2=input()

# Write your code below

a=list(set(s1)&set(s2))
a.sort()
if len(a) :
    print('The common letters are:')
    for i in a:
        print(i)
else:
    print('There are no common letters between them')

*/

