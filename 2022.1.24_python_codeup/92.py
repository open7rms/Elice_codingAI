n =int(input())
a=input().split()
d={}
for i in range(n) :
    a[i]=int(a[i])
for j  in range(1,24) :
    d[j]=0
print(d)
for k in range(n):
    d[a[k]]+=1

for l in range(1,24) :
    print(d[l],end=" ")
    
    
