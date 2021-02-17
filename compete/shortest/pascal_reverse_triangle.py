"""
0 1 2 3 4
 1 3 5 7 
  4 8 12
   12 20
---> 32

"""

n=int(input())
a=list(map(int,input().split()))
while n>1:
    for i in range(n-1):a[i]=a[i]+a[i+1]
    n-=1
print(a[0])


num = int(input())
base = [int(i)for i in input().split()]

while num>1:
    for i in range(num-1):
        base[i]=base[i]+base[i+1]
    num-=1

print(base[0])

