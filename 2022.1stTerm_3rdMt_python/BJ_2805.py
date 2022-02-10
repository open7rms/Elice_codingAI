from xmlrpc.client import _MultiCallMethod
import sys

#input
pilen,need=map(int,sys.stdin.readline().split())
piles=list(map(int,sys.stdin.readline().split()))

#length difference calculation
def diff(length,mid):
    value=0
    for i in range(len(length)):
        if (length[i]-mid) >0 :
            value +=length[i]-mid
    return value
#binery search engine
low=1
high=max(piles)
while low<=high :
    mid=(low+high)//2
    calNeed=diff(piles,mid)
    if calNeed >= need:
        low = mid+1
        #print("high",mid,diff(piles,mid),low)
    else :# calNeed < need:
        high =mid-1
        #print("low",mid,diff(piles,mid),high)
print(high)

#print(pilen,need,piles)