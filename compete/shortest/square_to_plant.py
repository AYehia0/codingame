""" 

John's task is to plant as many trees as he can in a square grid
One tree takes up 2x2 spaces
Input
An integer n Length of one side of a square
Output
An integer a The most number of trees John can plant
Constraints
2 < n < 50
Example
Input
2
Output
1


TIP: don't use int(2.5) to get 2 use // instead of

"""
print((int(input())//2)**2)
