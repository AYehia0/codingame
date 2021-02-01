"""

PROBLEM:
An ant on the floor can move 1 unit Left, Right, Forward, or Backward on each step.
Left, Right, Forward, and Backward are respectively denoted by L, R, F, and B. These directions are from the point of view of a fixed aerial observer.

You are given the steps of the ant. Calculate the Euclidean distance between the starting position and the final position of the ant.

Example input:
9
F F L R F R R R R

The ant moves three times forward and never backward, resulting in three vertical steps. It also moves once to the left and five times to the right, effectively resulting in four horizontal steps. The ant traveled sqrt(3²+4²) = 5 units.

The first line contains an integer n denoting the number of steps taken by the ant.
The second line contains n space separated letters L, R, F, and B denoting the step directions Left, Right, Forward, and Backward respectively.

Output the Euclidean distance dist between the starting position and the final position of the ant as an integer.
Test cases are designed such that dist is always an integer.
CONSTRAINS:
1 ≤ n ≤ 30
0 ≤ dist ≤ 20
EXAMPLE input:
2
B F
EXAMPLE output:
0
------------
2
B F
0
7
L L L L F F F
5
12
L R L R L R L R B F F B
0
20
L L L L L L L L R R B B B B L L B B B F
10


"""
import math


n = int(input())
f,b,l,r = 0, 0 ,0,0
for step in input().split():
    if step == 'F':
        f += 1
    if step == 'B':
        b += -1
    if step == 'L':
        l += -1
    if step == 'R':
        r += 1


right = l + r
up = f + b


print(int(math.sqrt(right**2 + up**2)))

# Another way it by making only 2 vars x,y and if it goes up increase y, down decrease y , right increase x, left decrease x
