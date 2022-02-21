import sys
from collections import deque
Nr = int(sys.stdin.readline())
stack = deque([])
for line in range(Nr) :
    command =input().split()
    if (command[0]=="push_front") :
        stack.appendleft(command[1])
    elif(command[0]=="push_back") :
        stack.append(command[1])
    elif(command[0]=="pop_front") :
        if(len(stack)==0):
            print(-1)
        else :
            print(stack.popleft())
    elif(command[0]=="pop_back"):
        if(len(stack)==0):
            print(-1)
        else :
            print(stack.pop())
    elif(command[0]=="size"):
        print(len(stack))
    elif(command[0] == "empty"):
        if(len(stack)):
            print(0)
        else :
            print(1)
    elif(command[0]=="front"):
        if(len(stack)==0):
            print(-1)
        else :
            print(stack[0])
    elif(command[0]=="back"):
        if(len(stack)==0):
            print(-1)
        else :
            print(stack[-1])
