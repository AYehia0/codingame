"""

Convert to bin


"""

n = int(input())
for i in range(n):

    x = int(input())
    # very nice way 
    print(f'{x:b}')

    # Another known way 
    print(bin(x)[2:])