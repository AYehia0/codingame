"""
Something
Somethin*
Somethi**
Someth*** 
Somet****
Some***** 
Som******
So*******
S********
*********
"""

word = input()
w = list(word)
print(word)

for i in range(1, len(word)+1):
    w[-1*i] = '*'
    print(''.join(w))

