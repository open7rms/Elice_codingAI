
# bineary search engine
def loop(low,high) :
    while low<=high :
        mid=int((low+high)/2)
        if search[mid] == same :
            return True
            break
        elif search[mid] > same :
            high =mid-1
        elif search[mid] < same :
            low= mid+1
#input module
searchn=int(input())
search =input().split()
for i in range(searchn):
    search[i]=int(search[i])
search.sort()

keyn=int(input())
key=input().split()
for i in range(keyn):
    key[i]=int(key[i])
# output module
for same in key :
    low =0
    high=len(search)-1
    
    if loop(low,high) :
        print('1')
    else :
        print('0') 
    
