loopn = int(input())

resultg=[]
for i in range(loopn) :
    productn = int(input())
    prices = list(map(int,input().split()))
    result =[]
    for price in prices :
        if price*0.75 in prices : 
            result.append(price*0.75)
    print(result) 
    resultg.append(result)
#print(resultg) 