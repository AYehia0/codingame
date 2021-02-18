"""
PROBLEM:
Given numbers s and d, output the largest d-digit number n such that the sum of its digits equals s. None of the digits in n may equal 0

One line: 2 integers, d and s

A d-digit integer n such that the sum of its digits add up to s
CONSTRAINS:
d ≤ s ≤ d*9
1 ≤ d
n ≥ 1
n does not contain the digit 0

Note: n can be larger than a 64-bit integer.
EXAMPLE input:
2 2
EXAMPLE output:
11
------------
2 2
11
3 21
993
4 36
9999
7 24
9921111
20 90
99999999711111111111
80 719
99999999999999999999999999999999999999999999999999999999999999999999999999999998

"""
d,s=map(int,input().split())

ans = ""
while d > 0:
    d-=1
    b=min(9,s-d)
    ans+=str(b)
    s-=b

print(ans)
   
