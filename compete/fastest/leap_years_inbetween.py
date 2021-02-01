"""

count the number of leep years in between 2 years


"""

a = int(input())
b = int(input())

count = 0
for i in range(a,b+1):
    if (i % 4) == 0:
        if (i % 100) == 0:
            if (i % 400) == 0:
                count += 1
            else:
               pass 
        else:
            count += 1
    else:
        pass

print(count)