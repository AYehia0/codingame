"""
PROBLEM:
You need to find all of the whole-numbered squares less than or equal to m, while ignoring all whole-numbered squares in i.

Line 1 : An integer m for the maximum number to check for whole-numbered squares.
Line 2 : A list i for whole-numbered squares you need to ignore.

Line 1 : Each whole-numbered square that you found, separated by spaces. 'None' if none are found.
CONSTRAINS:

EXAMPLE input:
50
9
EXAMPLE output:
1 4 16 25 36 49
------------
50
9
1 4 16 25 36 49
70
4 16 49
1 9 25 36 64
63
1 4 9 16 25 36 49
None
4
0
1 4

"""



l=input
x=print
m=int(l())
z=[int(i)for i in l().split()]
a=' '.join([str(i) for i in range(1,m+1)if i%pow(i,.5)==0and i not in z])
x(a)if a else x('None')

