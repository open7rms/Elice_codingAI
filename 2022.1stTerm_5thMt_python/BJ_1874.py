nrlength=int(input())
result=[]
que1=[int(i) for i in range(1,nrlength)]
que2=[]
queanswer=[]
que3=[]
for i in range(nrlength):
    result.append(int(input()))
result.reverse()
print(result)
for i in que1:
    if i ==result[i-1] :
        que2.append(i)
        queanswer.append("+push")
        print(queanswer,que2)
    else :
        #sub=result[i-1]-i
        for j in range(i,result[i-1]) :
            que2.append(i)
            queanswer.append("-push")
            print(queanswer,que2,j,result[i-1])
        for j in range(i,result[i-1]) :
            que3.append(que2.pop(-1))
            queanswer.append("pop")        
            print(queanswer,que3)
