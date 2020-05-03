# Generating Binomial Distribution
# Description
# Generate a binomial distribution, tested 10 times, given the number of trials(n) and probability(p) of each trial.

# The input will contain seed, n and p in the same order.

# The output should contain a numpy array with 10 numbers representing the required binomial distribution.

# Hint: You can use numpy's random number generator here too. Remember to set the seed before generating numbers to ensure correct output. [Please refer FAQ question at the bottom of this page]

# Sample Input:
# 0
# 10
# 0.5

# Sample Output:
# [5 6 5 5 5 6 5 7 8 5]

import numpy as np 
seed=int(input())
n=int(input())
p=float(input())

np.random.seed(seed)

#write your code here
s = np.random.binomial(n,p, 10)
print(s)
