import sys

listNr,qNr =map(int,input().split())
poketmon=[]
for i in range(listNr) :
    poketmon.append(sys.stdin.readline().rstrip("\n"))
for i in range(qNr):
    question=sys.stdin.readline().rstrip("\n")
    
    try :
        num=int(question)

    except :
        print(poketmon.index(question)+1)
    else :
        print(poketmon[num-1])
