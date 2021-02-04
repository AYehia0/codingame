"""

Given a non-negative amount N and a set of S coins of positive values Vi, return the number of ways to reach the required amount using the coins.

NB : You have an unlimited number of each coin at your disposal.

For example, given N = 10, S = 2 and the set of values V1 = {1, 5} , you should return 3. 

Indeed, there are 3 ways to sum coins of values {1, 5} up to 10 :

1*10, 5*2 and 1*5 + 5*1.

10 = 1 +1 +1 +1 +1 +1 +1 +1 +1 +1
10 = 5 + 5 
10 = 5 +1 +1 +1 +1 +1


"""
import math


coins = [1,5,2]
amount = 10

ans = [[0 for x in range(len(coins))] for x in range(amount+1)]

for i in range(len(coins)): 
    ans[0][i] = 1


for i in range(1, amount+1):
    for j in range(len(coins)):
        # Count of solutions including S[j] 
        x = ans[i - coins[j]][j] if i-coins[j] >= 0 else 0

        # Count of solutions excluding S[j] 
        y = ans[i][j-1] if j >= 1 else 0

        # total count 
        ans[i][j] = x + y
    

print(ans[-1][-1])