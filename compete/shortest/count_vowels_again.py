"""
------------
PROBLEM:
You must output the number of vowels in a string.
Y and y are not vowels!

A single line: A string str.

An integer: The number of vowels in the string.
CONSTRAINS:
0 < string length <= 100
EXAMPLE input:
Hello World!
EXAMPLE output:
3
------------
Hello World!
3
You're on the right track! Keep going.
11
This is the 3rd test.
4
I'm sure you will figure it out.
12

"""
# Can you solve using regex ?
# Actually test for is stupid and could be cheated by adding y to the letters, instead of using lower lol

print(sum(map(input().count,"aeiouy")))

# my sol 

print(len([i for i in input()if i in'aeiouy']))

