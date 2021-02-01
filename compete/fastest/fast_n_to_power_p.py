"""

PROBLEM:
Write last digit of number raised to the specified power.

Integer N to raise
Integer P power

Integer R
CONSTRAINS:

EXAMPLE input:
7
2
EXAMPLE output:
9
------------
7
2
9
7
16
5
6
123
15
1

"""

num = int(input())
power = int(input())

# Stupid way to do this 

print(str(num**power)[-1])

# Smart way, not the smartest
print(str((num%10)**power)[-1])

# Best way to do it

