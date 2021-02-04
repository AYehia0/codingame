"""

PROBLEM:
Description:
You are given a string that holds one or more letters. Each letter has a corresponding value such that A=1, B=2,…Z=26. You are to sum the values of the letter in the string, but should stop the summation when white-space, or the end of string is met.

Next, you should convert the sum to its binary form (base 2) and output that on the next line.

Last, you should output the maximum number of consecutive 1’s that occurred in the binary representation of the sum if it was even, and the maximum number of consecutive 0’s if the sum was odd.

Explanation:
ae = 6. A = 1, E = 5. 1 + 5 = 6. Sum = 6.
6 in binary is 110. Print '110'
6 is even so we search for the maximum number of consecutive 1’s.
That would be 2. Print '2'

Line 1: A string input holding some letters

Line 1: an integer sum representing the sum of all the letter positions in the alphabet, not indexes.
Line 2: the binary representation of the sum.
Line 3: the maximum occurrences of 1 or 0 depending on whether the sum is even or odd.
CONSTRAINS:
None
EXAMPLE input:
y
EXAMPLE output:
25
11001
2
------------
y
25
11001
2
aeiou
51
110011
2
aecdee
23
10111
1
zyxeeeee
100
1100100
2
z y x e e e e e
26
11010
2
AbCdExZ
65
1000001
5

"""

import string

y = string.ascii_lowercase


x = input().split()[0].lower()
# print(x)

x_index = sum([y.index(i)+1 for i in x])
x_bin = f'{x_index:b}'


print(x_index)
print(x_bin)

#checking if even or odd
if x_index%2==0:
    print(max(map(len,x_bin.split('0'))))
else:
    print(max(map(len,x_bin.split('1'))))