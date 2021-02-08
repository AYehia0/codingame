"""
PROBLEM:
Parse the regular hexagon, and tell how much regular unit triangle do you find, if the length of one side of the regular hexagon is n unit(s).

As it is well known, every regular hexagon, that has a positive integer value for the length of one side can be split into a positive integer value of regular triangles, where the regular triangle has sides with 1 unit of length.

For example, if the hexagon has sides with 1 unit of length, it will be split into 6 triangles.
If the hexagon has sides with 2 units of length, it will be split into 24 triangles.

Line 1: The length of one side of the hexagon is n unit

Line 1 : The number of regular 1-unit triangles inside the regular hexagon
CONSTRAINS:
0 < n < 7500
EXAMPLE input:
1
EXAMPLE output:
6
------------
1
6
3
54
5
150
10
600
50
15000
256
393216
3276
64393056


"""

n = int(input())

print(n**2*6)

