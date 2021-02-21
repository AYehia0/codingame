"""
INPUT:
1
Hello World !
------------
OUTPUT:
0
------------
INPUT:
2
l337 5p3k 15 c00l
5pr34d 7h3 w0rd !
------------
OUTPUT:
9
6
------------
INPUT:
2
abcd1234
a1b2c3d4
------------
OUTPUT:
4
4
------------
INPUT:
2
xxxxxxxxxx
1111111111
------------
OUTPUT:
0
10
------------

"""

n = int(input())
for i in range(n):
    row = input()
    co = 0
    for x in row:
        if x.isnumeric():
            co += 1
    print(co) 
    

