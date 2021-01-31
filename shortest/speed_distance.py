"""

PROBLEM:
You must output for each participant in a race the traveled distance (in meters) at a given speed S (centimeters/second) in given amount of time T (minutes).

Line 1: An integer N for the number of participants.
Next N lines: Two space separated integers S and T representing respectively the speed S and the time T.

N Lines: An Integer representing the distance traveled.
CONSTRAINS:
0 ≤ S ≤ 150
0 ≤ T ≤ 100000
EXAMPLE input:
1
20 10
EXAMPLE output:
120
------------
1
20 10
120
1
25 10
150
2
1 60
100 1
36
60
2
2 90
150 2
108
180
5
55 5
13 10
11 10
100 100
100 100000
165
78
66
6000
6000000
5
5 55
5 5
10 11
200 200
100 100000
165
15
66
24000
6000000
1
0 60
0
1
0 1000
0

"""

# my score is : 96

l=input
for i in range(int(l())):
    s,t=[int(j)for j in l().split()]
    print(int((t*0.6)*s))


# print([[int(j)for j in l().split()]for _ in range(int(l()))])