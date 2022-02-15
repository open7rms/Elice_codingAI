num = int(input())
numsum =0
for i in range(1,num+1) :
    numsum +=i
    if numsum>=num :
        print(numsum)
        break
