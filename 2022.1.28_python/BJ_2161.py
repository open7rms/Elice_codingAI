n=int(input())
count=1
arr=[]
for i in range(1,n+1) :
    arr.append(i)
answer=[]
while (len(arr)>0) :
    if count%2==0 :
        arr.append(arr.pop(0))
    else :
        answer.append(arr.pop(0))
    count+=1
for i in range(len(answer)) :
    print(answer[i],end=" ")
