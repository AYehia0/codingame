"""

PROBLEM:
A building company needs to know how many 90 degree corners there are so that they can buy the right numbers of corner brackets. They don't need to worry about angled corners!

All background is space character.

The building's plan view is represented in ASCII art. There is one continuous wall. A wall always has a space between it and a boundary or another wall.

Line 1 An integer W for the maximum width of the building
Line 2 An integer L for the maximum length of the building
Next L lines ASCII art representation of the building's plan

Line 1 Total number of 90 degree corners
CONSTRAINS:
4 ≤ W ≤ 42
4 ≤ L ≤ 42
EXAMPLE input:
5
5

 +-+
 | |
 +-+

EXAMPLE output:
4
------------
5
5

 +-+
 | |
 +-+

4
6
6

 ****
 *  *
 *  *
 ****

4
21
7

 #####     #####
 #   #     #   #
 #   #######   #####
 #                 #
 ###################

10
32
11

 ......      ......      ......
 .    ....   .    ...   ..    .
 ...     .....      .   .     .
   .                .....    ..
   .....                     .
       .......     ......    .
             .     .    .    ..
             .     .    .     .
             .......    .......

32
42
42

 !!!!!!!!!!          !!!!!!!!!!
 !        !    !!!   !        !    !!!!!!
 !!!!   !!!    ! !!!!!      !!!    !    !
    !   !      !            !    !!!  !!!
    !   !!!!!!!!       !!!!!!    !    !
 !!!!                  !       !!!    !!!
 !                !!!!!!       !        !
 !                !            !        !
 !!!!!!!!    !!!!!!        !!!!!    !!!!!
        !    !             !        !
   !!!!!!    !!!!!!    !!!!!      !!!
   !              !    !          !
 !!!              !!!!!!          !!!!
 !      !!!!!!            !!!!!!     !
 !      !    !            !    !     !!!
 !!!    !    !!!!!!!!!!!!!!    !       !
   !    !                      !  !!!!!!
   !    !                      !  !
   !    !                      !  !!!!!!!
 !!!    !!!!!!!           !!!!!!        !
 !            !           !             !
 !            !           !             !
 !!!!!        !           !             !
     !        !           !!!!!!    !!!!!
     !        !                !    !
     !        !                !    !
     !        !                !    !
     !        !                !    !
     !        !                !    !
     !!!!     !!!!             !    !
        !        !             !    !
        !        !             !    !
        !        !!!!      !!!!!    !!!
        !           !      !          !
        !           !      !          !
        !           !      !          !
     !!!!           !      !          !
     !              !      !          !
     !!!!!!!!!!!!!!!!      !          !
                           !!!!!!!!!!!!

96
20
10

 %%%%%%      %%%%%%
 %     %    %     %
 %      %  %      %
 %      %  %      %
 %      %  %      %
 %      %%%%      %
 %                %
 %%%%%%%%%%%%%%%%%%

6


"""


w = int(input())
l = int(input())

walls = []
for i in range(l):
    row = input().split()
    print(row)
    if len(row) > 0:
        walls.append(len(row))

print(walls)
# for l in walls:
#     if l





## Not mine 

# w = int(input())
# l = int(input())

# grid = []

# for i in range(l):
#     row = input()
#     grid += [row]

# c = 0

# for i in range(l):
#     for j in range(w):
#         if grid[i%l][j%w] != ' ' and grid[(i+1)%l][j%w] != ' ' and grid[(i+1)%l][(j+1)%w] != ' ':
#             c+=1

#         elif grid[i][j] != ' ' and grid[i+1][j] != ' ' and grid[i+1][j-1] != ' ':
#             c+=1
#         elif grid[i][j] != ' ' and grid[i][j+1] != ' ' and grid[i+1][j] != ' ':
#             c+=1
# print(c+1)