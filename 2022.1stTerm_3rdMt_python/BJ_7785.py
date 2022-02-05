
logn =int(input())
checker=dict()
for i in range(logn) :
      name, status= input().split()
      checker[name]=checker.get(name,0)+1

#print(checker)
stay=[]
for k,v in  checker.items():
      if v%2==1:
            stay.append(k)
#print(stay)
stay.sort(reverse=True)
#print(stay)
for name in stay:
      print(name)
