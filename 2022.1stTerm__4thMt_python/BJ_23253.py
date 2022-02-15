import sys
input=sys.stdin.readline
nBookTotal, nGroup=map(int,input().split())
BookSequence=[]
nBook=[]
#print(nBookTotal,nGroup)
for i in range(nGroup) :
    nBook.append(int(input()))
    BookSequence.append(list(map(int,input().split())))
#print(nBook,BookSequence)
#BookNum=[]

for index in range(1,nBookTotal+1) :
    for group in range(nGroup) :
        if len(BookSequence[group])>0 and index == BookSequence[group][-1]:
            #print("index",index,BookSequence[group][-1])
            BookSequence[group].pop(-1)

Bookleft=0
for group in range(nGroup) :
    Bookleft +=len(BookSequence[group])

if Bookleft==0 :
    print("Yes")
else :
    print("No")
