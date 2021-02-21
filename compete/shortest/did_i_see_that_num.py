"""
------------
INPUT:
7
1
1
3
1
3
2
3
------------
OUTPUT:
1
3
2
------------
INPUT:
6
9
-1
1
1
-1
-9
------------
OUTPUT:
9
-1
1
-9
------------
INPUT:
1
-1
------------
OUTPUT:
-1
------------
INPUT:
12
-3
-2
-1
0
1
2
3
4
5
6
7
8
------------
OUTPUT:
-3
-2
-1
0
1
2
3
4
5
6
7
8
------------
INPUT:
2
12
12
------------
OUTPUT:
12

"""

# using set is cool too 
s = []
n = int(input())
for i in range(n):
    x = int(input())
    if x not in s:
        s.append(x)
        print(x)

