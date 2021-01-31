"""

PROBLEM:
A Harshad number is an integer that is divisible by the sum of its own digits.
For example, 1729 is a Harshad number because 1 + 7 + 2 + 9 = 19 and 1729 = 19 × 91.

A positive integer N.

true if the integer is a Harshad number.
false If the integer is not a Harshad number.
CONSTRAINS:
0 < N < 10⁶
EXAMPLE input:
1229
EXAMPLE output:
false
------------
1229
false
18
true
154
false
45665
false
5
true


"""

# my try : 68 char

n=input()
print(['false','true'][int(n)%sum([int(i)for i in n])==0])

