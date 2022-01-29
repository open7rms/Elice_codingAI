n=int(input())
round=[]
for i in range(1,n+1):
    round.append(i)
    
print(round)
for i in range(1,n) :
    #round.pop((i**3)%(n-i)-1)
    print(round,round.pop((i**3)%(n-i+1)-1))
#print(round)














    

    
