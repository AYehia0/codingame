import math

n = int(input())
a = 1
for i in range(n):
    l = []
    for _ in range(i + 1):
        l.append(a)
        a += 1
    print(*l)