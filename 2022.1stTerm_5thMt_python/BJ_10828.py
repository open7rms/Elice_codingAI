commandNr=int(input())
stack=[]
result=[]
for commandi in range(commandNr) : 
    command=input().split()
    if(command[0]=="push") :
        stack.append(command[1])
    elif(command[0]=="pop") :
        if len(stack)==0:
            result.append(-1)
        else :
            result.append(stack.pop(-1))
    elif(command[0]=="size") :
        result.append(len(stack))
    elif(command[0]=="empty"):
        if len(stack)==0:
            result.append(1)
        else :
            result.append(0)
    elif(command[0]=="top"):
        if len(stack)==0 :
            result.append(-1)
        else :
            result.append(stack[-1])

for i in range(len(result)) :
    print(result[i])