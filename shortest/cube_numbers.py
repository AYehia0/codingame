"""

INPUT:
3 5
------------
OUTPUT:
5 6 7
6 7 8
7 8 9
------------
INPUT:
1 2
------------
OUTPUT:
2
------------
INPUT:
2 1
------------
OUTPUT:
1 2
2 3
------------
INPUT:
4 9
------------
OUTPUT:
9 10 11 12
10 11 12 13
11 12 13 14
12 13 14 15
------------
INPUT:
3 0
------------
OUTPUT:
0 1 2
1 2 3
2 3 4
------------
INPUT:
3 -1
------------
OUTPUT:
-1 -2 -3
-2 -3 -4
-3 -4 -5
------------

"""

n, q = [int(i) for i in input().split()]
neg = 1
for i in range(n):
    if q < 0:
        neg = -1
    print(' '.join([str(neg*i) for i in range(abs(q), abs(q)+n, 1)]))
    q = abs(q) + 1



