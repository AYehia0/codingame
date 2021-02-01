"""

PROBLEM:
You will be given N binary numbers.
Print the decimal sum of the odd numbers.

Line 1 N - number of binary values
Next N Lines binary numbers

sum of odd numbers, expressed in decimal
CONSTRAINS:
N<=100
0 <= each number <= 2^30
EXAMPLE input:
1
111
EXAMPLE output:
7
------------
1
111
7
5
101
100
11111
00000
0101010
36
10
10101010
11111111
00000000
01010101
11001100
00110011
01010101
10000111
01010101111
01010101010100000
1298
7
00110101010101001011010100
01010101010101010101010101
10000000000000000000000001
0111111111111111111111111111
100000000000000000000000
1000000000000000000000000
10000000000000000000010000001
458577366


"""

# my sol : 119 char

d = []
for i in range(int(input())):
    s = input()
    t = int(s, 2)
    if t%2!=0:
        d.append(t)
print(sum(d))


# Another shorter sol


