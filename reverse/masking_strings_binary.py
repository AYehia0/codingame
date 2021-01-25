""" 

The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01 Test 1


Input

00000 AAAAA xxxxx
01110 BBBBB xxxxx
01110 CCCCC xxxxx
01110 DDDDD xxxxx
00000 EEEEE XXXXX

###OUTPUT###

AAAAA
BxxxB
CxxxC
DxxxD
EEEEE

02 Test 2
Input

00000 First Error
00000 Bravo Avoid
00000 Third These
00000 Delta Other
00000 Fifth Words

###OUTPUT###

First
Bravo
Third
Delta
Fifth


03 Test 3
Input

11111 FALSE RIGHT
11111 WRONG RIGHT
11111 ERROR RIGHT
11111 UNFIT RIGHT
11111 FAILS RIGHT

###OUTPUT###

RIGHT
RIGHT
RIGHT
RIGHT
RIGHT


04 Test 4
Input

110 MNC ABo
111 abc def
010 GDI EHf
001 jkg Hil
101 JNk MLO

###OUTPUT###


ABC
def
GHI
jkl
MNO
05 Test 5

Input

00001 APPLY GRAPE
00010 BANCO KANJI
00100 CARES TOKEN
01000 DOTES HAZEL
10000 WAGER ELVES

###OUTPUT###

APPLE
BANJO
CAKES
DATES
EAGER

06 Test 6

Input

0000010111 MyNamUIToW DUrgvexsOz
1111110001 eCwfQtusKq ymandidJsi
0110100111 nPcfiinAyN FgOoKHbgsL
1010101000 moaOhMMWor olkVnEyNGJ
0111100101 kKBKSigpte xsYeMlihZy

###OUTPUT###

MyNameIsOz
ymandiusKi
ngOfKingsL
ookOnMyWor
ksYeMighty

07 Test 7

Input

101010011100001011111111000001 baabdcdcffffggghjjiillkkmmnnop abbacdcdeeeehhhgiijjkkllnnmmpo
000101100000011010011010110000 ppqrrqtsttuuvuxwwxyzyzbaaaccdd oorqqrstssvvuvwxxwzyzyabbbddcc
110000110100101001111100000100 ffffggggijjjlkklmnmmppppqqrqss eeeehhhhjiiikllknmnnoooorrqrtt
010001011100001011011001111011 tsuuvuwxwwyyzzbaaacdcdefeehggg stvvuvxwxxzzyyabbbdcdcfeffghhh
111110011111111110100011000110 jjiilklknnmmppoorqqrssssuuvuxw iijjklklmmnnooppqrrqttttvvuvwx

###OUTPUT###

aabbccddeeffgghhiijjkkllmmnnoo
ppqqrrssttuuvvwwxxyyzzaabbccdd
eeffgghhiijjkkllmmnnooppqqrrss
ttuuvvwwxxyyzzaabbccddeeffgghh
iijjkkllmmnnooppqqrrssttuuvvww

"""

sol = []

for i in input().split(" "):
    sol.append(i)
    print(sol)