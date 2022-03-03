import sys

listNr,qNr =map(int,input().split())
poketmon=[]
for i in range(listNr) :
    poketmon.append(sys.stdin.readline().rstrip("\n"))
for i in range(qNr):
    question=sys.stdin.readline().rstrip("\n")
    if question in poketmon :
        print(poketmon.index(question)+1)
    else :
        print(poketmon[int(question)-1])
