"""
Given a list of W words, concatenate them together to form an NxN grid and return the two words on the main diagonals (top to bottom) in alphabetical order.

Line 1: The size N of the grid.
Line 2: The number of words W.
Next W lines: The word list.

One line with the two diagonal words, space separated and in alphabetical order.
CONSTRAINS:
3 ≤ N ≤ 20
W ≤ 100
EXAMPLE input:
3
3
cow
bat
rat
EXAMPLE output:
cat war
------------
3
3
cow
bat
rat
cat war
5
5
sack
cute
harbour
skull
elite
choke stole
8
10
magical
academy
bail
reasoning
golden
alliance
auto
negotiate
alert
angel
absolute marginal
10
19
sack
absent
atrocity
eager
acid
cabin
bail
habitat
ownership
globe
absorb
lane
abuse
odds
arena
gallon
prey
acre
array
strawberry technology
15
36
tackle
absent
fake
racial
absurd
icon
ultimate
annually
sack
abundance
abstract
challenging
wander
abuse
acid
domain
academy
accordance
accelerate
tactic
accent
ease
habitat
amid
acre
aide
accountable
banner
adequate
acute
aids
absorb
adverse
sacred
alert
bass
kindheartedness trustworthiness
20
57
backdrop
abortion
accumulate
absence
abuse
nest
cabin
absent
acid
canal
sketch
absorb
adhere
accommodate
acre
abstract
alien
absurd
racial
abundance
aide
academy
accent
aside
accelerate
accused
tactic
acceptance
aids
deed
accessible
adjust
array
accidentally
aspire
fabric
accomplish
sack
auction
accumulation
adolescent
activist
accomplishment
accordance
adverse
alliance
accuracy
archive
ladder
activate
beam
albeit
abolish
amusing
yell
accountable
badge
buckminsterfullerene uncharacteristically

"""

# cat war
# choke stole

# Not shortest but this is the my first solution to the problem

grid_size = int(input())
word_length = int(input())
big_str = ''
first_side = ''
second_side = ''
ans = []

for i in range(word_length):
    row = input()
    big_str += row

n = grid_size-1 
x = 0
while n < grid_size*grid_size -1 and x < grid_size*grid_size:
    first_side += big_str[n]
    second_side += big_str[x]
    x += grid_size+1
    n += grid_size-1


ans.append(first_side)
ans.append(second_side)

print(' '.join((sorted(ans))))

