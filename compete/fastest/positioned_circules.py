"""
PROBLEM:
You are given a number of circles assuming that none are positioned on top of each other. What is the most number of points that they will intersect at? For example 3 circles: 6 points

One int x the number of circles

One int y the maximum number of intersecting points
CONSTRAINS:
1<x<1000000000
EXAMPLE input:
3
EXAMPLE output:
6
------------
6
15
210
1000001
1000001000000
55
2970

"""

x = int(input())

print(x*(x-1))
