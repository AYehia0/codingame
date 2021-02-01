"""

INPUT:
6
4
------------
OUTPUT:
360
------------
INPUT:
4
4
------------
OUTPUT:
24
------------
INPUT:
7
3
------------
OUTPUT:
210
------------
INPUT:
2
1
------------
OUTPUT:
2
------------
INPUT:
18
18
------------
OUTPUT:
6402373705728000
------------
INPUT:
10
9
------------
OUTPUT:
3628800
------------
INPUT:
10
2
------------
OUTPUT:
90
------------
INPUT:
4
2
------------
OUTPUT:
12
------------
INPUT:
15
1
------------
OUTPUT:
15
------------

"""


x = int(input())
n = int(input())
a=1
for b in range(n):
    a = a * x
    x=x-1
print(a)
