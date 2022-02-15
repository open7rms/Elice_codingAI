loopn = int(input())

resultg=[]
for i in range(loopn) :
    productn = int(input())
    prices = list(map(int,input().split()))
    result =[]
    while(len(prices)) :

        if prices[0]*4/3 in prices : 
            prices.pop(prices.index(prices[0]*4/3))
            result.append(prices.pop(0))
            
        else :
            prices.pop(0)
    #print(result) 
    resultg.append(result)
for i in range(loopn):
    print("Case #{}:".format(i+1,),end=" ") 
    for j in range(len(resultg[i])):
        print(resultg[i][j],end=" ")
    print()