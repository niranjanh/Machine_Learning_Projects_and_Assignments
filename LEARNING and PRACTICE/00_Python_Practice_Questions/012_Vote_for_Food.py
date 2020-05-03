/*

Vote for Food
Your team is going for camping and you are taking a vote to decide what food to pack for dinner.
Everyone gets a vote and the food item that gets at least one more than half of the votes wins. None of the items wins if nothing gets at least one more than half votes. Assume that every person gets only one vote.
The input will contain a list of food items where each occurrence of an item represents one vote. You should print the winning food item as output. If there is no clear winner, print "NOTA". 

Sample Input:
["pasta","pasta","pasta","pasta","pasta","paratha","paratha","paratha"]
Sample Output:
pasta

*/


import ast,sys
input_str = sys.stdin.read()
votes = ast.literal_eval(input_str)


foodDict = dict()

for food in votes:
    c = foodDict.get(food, 0)
    foodDict[food] = c + 1
    
maxVotes = 0
wonFood = ""
for key, item in foodDict.items():
    if item > maxVotes:
        maxVotes = item
        wonFood = key

tie = False
for key, item in foodDict.items():
    if key != wonFood and maxVotes == item:
        tie = True
        break
    
if not tie:
    print(wonFood) 
else: 
    print("NOTA") 

        
    
