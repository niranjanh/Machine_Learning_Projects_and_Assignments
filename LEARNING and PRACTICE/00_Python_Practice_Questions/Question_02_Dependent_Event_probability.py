# Coloured cards
# Description
# A card stack contains white and black cards. Two cards are drawn randomly without replacement. The probability of selecting a white and then a black card is x. The probability of selecting a white card in the first draw is y. You have to find the probability of drawing a black card, given that the first card drawn was white.
# The input will contain two lines with x and y respectively.  
# The output should be displayed as a float(no need to round it off).
# Sample Input:
# 0.2
# 0.5
# Sample Output:
# 0.4

x=float(input())
y=float(input())
#write your code here

# W -  prob of white ball
# B -  prob of black ball
# P(W then B) = P(W and B) = x
# P(W) = y
# to find P(B then W) = P(B and W)
# = P(W then B) / P(W) 
#  here x/y

print(x/y)


