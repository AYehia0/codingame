"""  
PROBLEM:
A web color is represented by a number sign #, followed by three bytes, each of them represented by two hexadecimal digits, which are the rate of each Red, Green and Blue color (between 0 and 255).
You are given a hexadecimal triplet, and you have to return the value of each RGB color rate.

Line 1: A hexadecimal triplet (three bytes, one per color): #RRGGBB

Line 1: The red rate (0-255) in base 10
Line 2: The green rate (0-255) in base 10
Line 3: The blue rate (0-255) in base 10
CONSTRAINS:
Each input character (excepted #) is a hexadecimal digit (0-9, A-F)
EXAMPLE input:
#FF0000
EXAMPLE output:
255
0
0
------------
#FF0000
255
0
0
#000000
0
0
0
#373737
55
55
55
#A59B87
165
155
135
#C000DE
192
0
222

"""

c=input()[1:]
for i in[0,2,4]:
    print(int(c[i:i+2],16))
