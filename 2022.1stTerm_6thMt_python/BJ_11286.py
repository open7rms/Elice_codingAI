import sys
import heapq

total=int(input())
heap=[]
for i in range(total) :
    num=int(sys.stdin.readline())
    
    if num ==0:
        if(len(heap)==0):
            print('output=',0)
        else :
            sameN=int(heap.count(heap[0]))
            
            if sameN>1 :
                #print('sameN',sameN)
                small=pow(2,31)
                for j in range(sameN):
                    if small>int(heap[j][1]):
                        #print('loop',j,heap[j][1])
                        small=heap[j][1]
                
                if small !=0 :
                    ind=heap.index((heap[0][0],small))
                    value=heap.pop(ind)
                    print('output=',ind,value[1])
            else :
                value=list(heapq.heappop(heap))
                print('output=',value[1])
            
    else : 
        heapq.heappush(heap,(abs(num),num))