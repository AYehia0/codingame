""" 


A standard chessboard consists of 8×8 = 64 squares of alternating color. Each square's "name" is composed of its file (a-h) and rank (1-8), with a1 denoting the dark square at the bottom-left.

Given the names of N squares, print whether each is dark or light.
Input
Line 1: N, the number of squares to follow
Next N lines: square names
Output
The color of each square (either dark or light), one per line.
Constraints
1 ≤ N ≤ 64
Example


Input: 
1
h1

Output:
light


print'dlairgkh t'[sum(map(ord,input()))%2::2]


first Idea : to construct a matrix like the chess board
to draw 1 row : ["-"] * 8

['-', '-', '-', '-', '-', '-', '-', '-']

to draw 8x8 : [ ["-"]*8 for _ in range(8) ]

[
8    ['-', '-', '-', '-', '-', '-', '-', '-'], 
7    ['-', '-', '-', '-', '-', '-', '-', '-'], 
6    ['-', '-', '-', '-', '-', '-', '-', '-'], 
5    ['-', '-', '-', '-', '-', '-', '-', '-'], 
4    ['-', '-', '-', '-', '-', '-', '-', '-'], 
3    ['-', '-', '-', '-', '-', '-', '-', '-'], 
2    ['-', '-', '-', '-', '-', '-', '-', '-'], 
1    ['-', '-', '-', '-', '-', '-', '-', '-']
    ]
       a    b    c    d    e    f    g    h

a5 ---> [5][a]

abcdefgh
now we have to figure out how to assign 'light' and 'dark' to the board
we know that it's like : 'dark', 'light', 'dark', 'light', 'dark', 'light', 'dark', 'light' 

we can create the board by :[ [ ["light", "dark"][((i+j)%2)] for i in range(8) ] for j in range(8) ]
create array of arrchays/rows : i%1,2,3,4...8 = 0,1,0,1,0,1 etc

let's assume that the given index is h7 ---> [7][h]

since the last element in the list is 8,8 and the list starts with 0 to 7

so Y-axis would be 7-1 = 6 
and X-axis would be ord('h')-98 = 104 - 97 = 7, it's true since 7 is the last elemnt in the list

chr(97) = a : the first char of the ascii chars  so ord(given_index) - ord(first_index_chess) = X-axis

"""

#board =[ [ ["light", "dark"][(i+j)%2] for j in [0,1]*4 ] for i in [0,1]*4 ]



#constucting the board
another_board = [ [ ["dark", "light"][((i+j)%2)] for i in range(8) ] for j in range(8) ]

index = 1
y = "h"

print(f"Index : ({ord(y) -97},{index-1})")
print(another_board[index-1][ord(y)-97])

