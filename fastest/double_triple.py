"""

given a string double the letter the second time it appears, triple the third time it appears


"""

x = input()
z = []
d = {}
for c in x:
    k = d.get(c, 0) + 1
    print(k)
    d[c] = k
    z += [c * k]
print(*z, sep = '')
