"""

Given two numbers, A and B, return the number of squares between A and B inclusive.

Between A = 1 and B = 9 inclusive are 3 squares: 1, 4, and 9
Between A = 10 and B = 25 inclusive are 2 squares: 16 and 25
Between A = 26 and B = 35 inclusive are 0 squares


"""

import math

a = int(input())
b = int(input())

ans = math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1
print(ans)


# Another way 

t=0
for i in range(a,b+1):
    if math.sqrt(i)==int(math.sqrt(i)):
        t+=1
        
print (t)