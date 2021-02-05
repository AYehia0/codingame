"""
PROBLEM:
Match all the numbers from the first list of letters to all of them in the second. If a character only is in the first list, output 'NONE' instead of where that numbers is on the second list. You can only match one character once. First output the index of where the first character of the first list is on the second list (index starts from 0). Next, do the same thing except by doing it with the second character. Then the third and all the others. The length of the lists are length

Example:
If length is 3 and the next inputs are:
A B C
B A C
Then output:
1
0
2

Line 1: An integer length for the length of the list.
Line 2: length space separated strings part1 for the first list.
Line 3: length space separated strings part2 for the second list.

The indexes of where the characters are on the first list in the second.
CONSTRAINS:
1 ≤ length ≤ 10
part1 and part2 contain only uppercase letters.
EXAMPLE input:
3
A B C
B A C
EXAMPLE output:
1
0
2
------------
3
A B C
B A C
1
0
2
3
H R O
O H R
1
2
0
3
G T D
F S T
NONE
2
NONE
3
I O I
I O O
0
1
NONE
5
D G S H X
V D G S G
1
2
3
NONE
NONE


"""



import sys
import math

length = int(input())
part_1 = []
part_2 = []
ind = []
for i in input().split():
    part_1.append(i)
for i in input().split():
    part_2.append(i)

for i in part_1:
    try:
        print(part_2.index(i))
        part_2[part_2.index(i)] = ' '
    except ValueError:
        print('NONE', sep=' ')

