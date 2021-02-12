"""
PROBLEM:
The Waiter Niki daily works for a pittance. After a hard day, he wants to treat himself to a drink. But he can only afford that with a decent tip. So if he gets more than a certain percentage of the tip in total on one day that he can drink until he forgets the f*** job.

Line 1: An integer N for the number of tables he served.
Line 2: An integer percentage for the percentage of the bill he needs as tip to get drunk.
Next N lines: Two space-separated floats bill for the amount of the bill and tip for the amount of the tip.

The Waiter is drunk or not: "DRUNK" / "THIRSTY".
CONSTRAINS:
0 < N < 50
0 ≤ percentage , tip ≤ 100
0 ≤ bill ≤ 1000
EXAMPLE input:
1
10
10 1
EXAMPLE output:
DRUNK
------------
1
10
10 1
DRUNK
1
20
15 1.5
THIRSTY
4
15
15 4.50
80 10
5 0
10 2
DRUNK
8
12
50 5
69.69 7
25 3
9.99 1.01
5.45 0.6
36 4
1.20 1
99.90 14
THIRSTY

"""

n = int(input())
p =int(input())
x = y = 0
for _ in range(n):
    b, t = map(float, input().split())
    x += b
    y += t
print(("THIRSTY","DRUNK")[p<=100*y/x])
