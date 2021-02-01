"""

PROBLEM:
Your program must read the string given on the standard input and print to the standard output the same string converted into 1337 speak.

To convert text into 1337 speak, one must replace (whether upper or lower case):
'O' with '0'.
'L' with '1'.
'Z' with '2'.
'E' with '3'.
'A' with '4'.
'S' with '5'.
'G' with '6'.
'T' with '7'.
'B' with '8'.
'Q' with '9'.

A string S.

S converted to 1337 speak.
CONSTRAINS:
S contains at least 1 character.
EXAMPLE input:
Hello World
EXAMPLE output:
H3110 W0r1d
------------
Hey
H3y
CodinGame
C0din64m3
Hello World
H3110 W0r1d
abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
48cd3f6hijk1mn0p9r57uvwxy2 48CD3F6HIJK1MN0P9R57UVWXY2


"""

# 140 char

d={'O':'0','L':'1','Z':'2','E':'3','A':'4','S':'5','G':'6','T':'7','B':'8','Q':'9'}
s=input()
print(''.join([d.get(i.upper(),i)for i in s]))