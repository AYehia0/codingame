"""
INPUT:
1
------------
OUTPUT:
1
------------
INPUT:
2
------------
OUTPUT:
1 2
------------
INPUT:
10
------------
OUTPUT:
1 2 5 10
------------
INPUT:
9
------------
OUTPUT:
1 3 9
------------
"""

n = int(input())
ans = []
for i in range(1,n+1):
    # use n%i == 0 instead 
    if n/i == int(n//i):
        ans.append(str(i))

print(*ans)
