s=input()
print(''.join([s[x:x+2][::-1]for x in range(0,len(s),2)]))
