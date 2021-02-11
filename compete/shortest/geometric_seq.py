"""
PROBLEM:
A geometric sequence, is a sequence of numbers where each term after the first is found by multiplying the previous one by a number called the common ratio.

Your program must print the N first numbers of a geometric sequence of ratio R and started by 1.

Two space separated integers N and R.

The first N integers of the geometric sequence of common ratio R, starting with 1.
CONSTRAINS:
0 < N < 50
0 ≤ R ≤ 50
Each integer of the suite can hold in a 64 bits integer.
EXAMPLE input:
5 2
EXAMPLE output:
1 2 4 8 16
------------
5 2
1 2 4 8 16
3 2
1 2 4
6 3
1 3 9 27 81 243
3 0
1 0 0
7 42
1 42 1764 74088 3111696 130691232 5489031744
40 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
"""

# not the shortest

n,r=[int(i)for i in input().split()]
x,y=0,1
a=['1']
while x<n-1:
  y *= r;a+=[str(y)];x+=1
print(' '.join(a))
