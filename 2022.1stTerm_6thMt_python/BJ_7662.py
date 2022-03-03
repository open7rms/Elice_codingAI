import sys
loop=int(input())

for i in range(loop) :
    inloop=int(input())
    print(inloop)
    que=[]
    for i in range(inloop) :
        op, num =sys.stdin.readline().split(" ")
        #print (op, num)
        if op =="I" :
            que.append(int(num))
        elif op =="D" and num =="-1" :
            if(len(que)==0):
                continue
            que.pop(que.index(min(que)))
        else :
            if(len(que)==0):
                continue
            que.pop(que.index(max(que)))
    if len(que)==0 :
        print('Empty')
    else :
        print('output ',max(que)," ",min(que))