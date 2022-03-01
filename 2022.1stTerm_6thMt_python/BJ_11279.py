import sys
import heapq
#input = sys.stdin.readlines
operation=int(input())
seq=[]
for i in range(operation) :
    num=int(sys.stdin.readline())
    heapq.heappush(seq,(-num,num))
    if num ==0 :
        print(heapq.heappop(seq)[1])
