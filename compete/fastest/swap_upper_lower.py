"""

Swap upper case to lower and lower to upper and


"""

s=input()
print(''.join(x.lower() if x.isupper() else x.upper() for x in s))


# another cool solution is to use the swapcase()

print(s.swapcase())