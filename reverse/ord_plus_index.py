"""

INPUT:
codingame
------------
OUTPUT:
cpflrlgtm
------------
INPUT:
abcdef
------------
OUTPUT:
acegik
------------
INPUT:
cracker
------------
OUTPUT:
cscfojx
------------
INPUT:
aaaaaa
------------
OUTPUT:
abcdef
------------

"""

l = input()
ans = []
for j,i in enumerate(l):
    ans.append(chr(ord(i)+j))

print(''.join(ans))
