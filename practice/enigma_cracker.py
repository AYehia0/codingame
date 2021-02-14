import sys
import math
import string 

words = string.ascii_uppercase

operation = input()
pseudo_random_number = int(input())
rotors = []
for i in range(3):
    rotor = input()
    rotors.append(rotor)
message = input()

to_fix = list(message)

print(to_fix[0])

# first position 
z = ord(to_fix[0]) + pseudo_random_number
f = chr(z)

first = [f]
print(first)

for i in range(1, len(message)):
    z = ord(f) + 1
    first.append(chr(z))
    f = chr(z)

print(first)
# first rotor 
rotor1 = ''
for i in first:
    rotor1 += rotors[0][words.index(i)]


# second rotor 
rotor2 = ''
for i in rotor1:
    rotor2 += rotors[1][words.index(i)]

# third rotor 
rotor3 = ''
for i in rotor2:
    rotor3 += rotors[2][words.index(i)]


print(rotor3)
