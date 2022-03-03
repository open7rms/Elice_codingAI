import sys
import heapq
loop=int(input())

for i in range(loop) :
    inloop=int(input())
    #print(inloop)
    que=[]
    for i in range(inloop) :
        op, num =sys.stdin.readline().split(" ")
        #print (op, num)
        if op =="I" :
            heapq.heappush(que,int(num))
        elif op =="D" and int(num) == -1 :
            
            if(len(que)==0):
                continue
            heapq.heappop(que)

        else :
            if(len(que)==0):
                continue
            #print('before',que)
            que=heapq.nlargest(len(que),que)[1:]
            heapq.heapify(que)
            
    if len(que)==0 :
        print('Empty')
    else :
        smallest=que[0]
        biggest =heapq.nlargest(len(que),que)[0]
        print(biggest,smallest)