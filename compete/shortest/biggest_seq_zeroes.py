"""

Find biggest seq of zeros in strings

for example: 100230400002
2 1 4 
so 4 is the longest sequence


"""
x = input()
m=0
z=0
for i in x:
 z+=1 if i=='0'else-z
 m=max(m,z)
print(m)


y=0
for i in x:
    if i=='0':
        z += 1
    else :
        z-=1
    y=max(y,z) 

print(m)