total=int(input())
a=[]
for i in range(total) :
    a.append(int(input()))

view=0
count=0
for i in range(total-1,-1,-1):
    if a[i]>view :
        view=a[i]
        count +=1
print(count)
