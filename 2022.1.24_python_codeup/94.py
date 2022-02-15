n=int(input())
a=input().split()
minnum=int(a[0])
for i in range(n):
    if int(a[i])<minnum :
        minnum=int(a[i])
print(minnum)
