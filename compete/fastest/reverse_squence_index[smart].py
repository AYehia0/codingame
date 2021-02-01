"""


(N) index

5 3
sequence from 0 to N-1
0 1 2 3 4 

!) reverse : 4 3 2 1 (0)
2) reverse : 1 2 3 (4) (0)
3) reverse : 3 2 (1) (4) (0)
4) reverse : 2 (3) (1) (4) (0)

now print the index

idk the question ,,, lol

"""

l, n = [int(i) for i in input().split()]

i = n

while i<l:
    i = l -i -1
    l-= 1
print(i)