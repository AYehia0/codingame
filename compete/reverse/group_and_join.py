"""

------------
INPUT:
10
abcabcabcb
------------
OUTPUT:
aaa
bbbb
ccc
------------
INPUT:
19
.a!/3bghpoppggadrff
------------
OUTPUT:
aa
b
d
ff
ggg
h
o
ppp
r
------------
INPUT:
27
AcBcayOpPbJj.%Ss$EaaaAQuopZ
------------
OUTPUT:
aaaaaa
bb
cc
e
jj
oo
ppp
q
ss
u
y
z
------------
INPUT:
119
uUFNsojSAOGMKOEK57$=ksmkfosmOFMpswpKFkfpsKpvkpDPgfdpkGpKDogdmcmvomdrOMVODVPkp485(SLfmvxpcWvmxlmXVEOvmvP12”4mfcxpworghjA
------------
OUTPUT:
aa
ccc
dddddd
ee
ffffffff
ggggg
h
jj
kkkkkkkkkkk
ll
mmmmmmmmmmmmm
n
ooooooooooo
ppppppppppppp
rr
sssssss
uu
vvvvvvvvv
www
xxxx
------------

"""



from collections import Counter

n = int(input())
s = input()
ans = []
for i in s:
    if i.isalpha():
        ans.append(i)

c = Counter([ i.lower() for i in ans ] )

result = [key * value for key, value in c.items()]

print('\n'.join(sorted(result)))


# another way by : dv_man
n = int(input())
s = input().lower()

letters='abcdefghijklmnopqrstuvwxyz'

for c in letters:
    a=0
    for l in s:
        if c == l:
            a+=1

    if a>0:
        print(c*a)
