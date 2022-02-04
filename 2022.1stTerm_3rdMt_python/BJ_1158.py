n,hop = input().split()

arr=[]
for i in range(1,int(n)+1) :
      arr.append(i)
result=[]
current=0

while len(arr)>0 :
      current = (current+ int(hop)-1)%len(arr)
      result.append(arr.pop(current))
            
print(result)            
