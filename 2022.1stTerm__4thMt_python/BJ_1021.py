stackSize,outNr = map(int,input().split())
stack =[] 
for i in range(1,stackSize+1) :
    stack.append(i)
sequence= list(map(int,input().split()))#.insert(0,0)
count = 0
for Nr in range(outNr):
    print(stack.index(sequence[Nr]))
    if(stack.index(sequence[Nr])>=(len(stack)-stack.index(sequence[Nr]))):
        print(">", len(stack)-stack.index(sequence[Nr]))
        count +=len(stack)-stack.index(sequence[Nr])
    else : 
        print("<",stack.index(sequence[Nr]))
        count +=stack.index(sequence[Nr])
    stack.pop(stack.index(sequence[Nr]))
print("count",count)    
#print(stack,sequence)