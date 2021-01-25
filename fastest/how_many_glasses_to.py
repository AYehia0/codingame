"""

find the number of glasses one can hit in a resturant,, idk i forgot to scrap lol

if there are 2 people one hit
3 people  3 hits 

"""

import math

x = input()

print(math.comb(x,2))


# Other way is to count 
print(sum(range(int(x))))

