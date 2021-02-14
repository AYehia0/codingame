"""
------------
PROBLEM:
Your program must insert the given operator (+, -, / or *) at index X of an integer number and output the result of the operation.

The operation is always valid and the result is always an integer. Plus "+" and minus "-" are the only operators that can be inserted at index 0.

A character O, an integer X and an integer N, separated by spaces. O is a mathematical operator from +, -, / and *.

The result of the operation obtained by inserting O in N at index X.
CONSTRAINS:
-1 000 000 000 < X, N < 1 000 000 000
EXAMPLE input:
- 2 123
EXAMPLE output:
9 (12 - 3)
------------
- 2 123
9
- 0 42
-42
+ 3 555000
555
+ 0 1
1
- 4 123456
1178
* 5 100001
10000
/ 1 62
3

"""

inputs = input().split()
o = inputs[0]
x = int(inputs[1])
n = list(inputs[2])

n.insert(x, o)
print(int(eval(''.join(n))))

