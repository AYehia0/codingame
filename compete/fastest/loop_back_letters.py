"""
PROBLEM:
Print n letters of the alphabet in order and starting from the letter s. Letter case should be the same as letter s. Wrap back to the start of the alphabet after 'z' or 'Z'.

Line 1: An integer n for the number of letters to print.
Line 2: The starting letter s.

An alphabet string n letters long starting from letter s, in the same case as s.
CONSTRAINS:
1 ≤ n ≤ 100
s is a character (lower or upper case)
EXAMPLE input:
3
a
EXAMPLE output:
abc
------------
abc
4
z
zabc
2
J
JK
27
b
bcdefghijklmnopqrstuvwxyzab
10
f
fghijklmno
100
A
ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUV
1
h
h


"""


import string


letters_l = string.ascii_lowercase
letters_u = string.ascii_uppercase


n = int(input())
s = input()

start = s[0]

for i in range(n):
    print(letters_l[ letters_l.index(start) ])
    
