"""

------------
INPUT:
MAM
------------
OUTPUT:
J
------------
INPUT:
JFMAMJJASON
------------
OUTPUT:
D
------------
INPUT:
OND
------------
OUTPUT:
J
------------
INPUT:
FMAMJJASONDJFMAMJJASONDJFMAMJJASONDJ
------------
OUTPUT:
F
------------
INPUT:
O
------------
OUTPUT:
N
------------

"""

months = input()

# stupid solution
M = 'JFMAMJJASOND'*10

print(M[(M.find(months)+len(months))])
