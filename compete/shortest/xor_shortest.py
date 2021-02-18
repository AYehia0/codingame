"""
PROBLEM:
Your program must perform a binary XOR on two binary numbers given through the standard input and print the result to the standard output.

XOR Truth Table
Input Output
A B
0 0 0
0 1 1
1 0 1
1 1 0

Warning, the number of binary digits must remain the same.

2 binary numbers n1 and n2, separated by spaces.

The result of a XOR between n1 and n2.
CONSTRAINS:
n1 and n2 have the same number of digits.
EXAMPLE input:
001 011
EXAMPLE output:
010
------------
0 1
1
001 011
010
011 001
010
00000000000111 10101010111100
10101010111011

"""


#MrAlpha
print(*(int(a)^int(b)for a,b in zip(*input().split())),sep='')


# My code
n,m=input().split()
a=''
for i in range(len(n)):
 a+=str(int(n[i])^int(m[i]))
print(a)
