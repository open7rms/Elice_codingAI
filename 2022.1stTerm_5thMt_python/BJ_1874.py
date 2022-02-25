
nrlength=int(input())
result=[]

stack = []
counter =1
for i in range(nrlength) :
    num = int(input())
    while counter<=num :
        stack.append(counter)
        counter+=1
        result.append('+')
    if num ==stack[-1]:
        stack.pop()
        result.append('-')
    else :
        print('No')
        exit(0)

for i in result : 
    print(i)