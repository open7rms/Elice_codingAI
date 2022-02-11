round=int(input()) # # of test case
def diff(a,b): #function diff 왼쪽으로 가는 차는 왼쪽 바퀴의 시간이 오른쪽 바퀴의 시간보다 이르다.
    return a-b
result =[] #출력할 결과값 list

for i in range(round):
    count=int(input()) # # of time log
    x=list(map(int,input().split())) # left tire time log
    y=list(map(int,input().split())) # right tire time log
    #print(x,y)
    count =0
    for i in list(map(diff,x,y)) :
        if i <0 : count +=1 # 왼쪽으로 가는 차량의 # of time log
    result.append(count)   
for i in result : # print function
    print(int(i/2))   # one car has two time-logs
