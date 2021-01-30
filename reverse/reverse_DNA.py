"""

------------
INPUT:
ACGT
------------
OUTPUT:
TGCA
------------
INPUT:
A
------------
OUTPUT:
T
------------
INPUT:
C
------------
OUTPUT:
G
------------
INPUT:
G
------------
OUTPUT:
C
------------
INPUT:
T
------------
OUTPUT:
A
------------
INPUT:
GATTACA
------------
OUTPUT:
CTAATGT
------------

"""

# Stupid fast 

dna = input()

s = ''

for i in dna:
    if i == 'A':
        s += 'T'
    if i == 'C':
        s += 'G'
    if i == 'G':
        s += 'C'
    if i == 'T':
        s += 'A'

print(s)
