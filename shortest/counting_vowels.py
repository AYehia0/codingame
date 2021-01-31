"""
PROBLEM:
You must output the count (case-insensitive) of all English vowels (A, E, I, O, U) in a string.

Line 1: A string s for you to operate on.

Line 1: A count of each vowel in alphabetical order separated by a space.
CONSTRAINS:
length of s ≤ 64
EXAMPLE input:
ABCDEFGHIJKLMNOPQRSTUVWXYZ
EXAMPLE output:
1 1 1 1 1
------------
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1 1 1 1 1
Uppercase and lowercase!
3 4 0 1 1
C0dInG4me
0 1 1 0 0
BlackAndYellow
2 1 0 1 0

"""
# s=input().lower()
# print(*[s.count(b)for b in'aeiou'])

# Another intersting sol by WVN

d=dict(zip('AEIOU',[0]*5))

for l in input().upper():
 if l in d:
    d[l]+=1
print(*d.values())