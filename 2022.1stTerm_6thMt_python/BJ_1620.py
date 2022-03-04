import sys

listNr,qNr =map(int,input().split())
poketmon=dict()
poketmonL=[]
for i in range(listNr) :
    mon=sys.stdin.readline().rstrip("\n")
    poketmon[mon]=i+1
    poketmonL.append(mon)

for i in range(qNr):
    question=sys.stdin.readline().rstrip("\n")
    
    try :
        num=int(question)

    except :
        print(poketmon[question])
    else :
        print(poketmonL[num-1])
