num=int(input())
lines=[]
temp=[]
for i in range(num) :
    lines.append(input())

for i in range(len(lines)) :
    temp=lines[i].split()
    temp.reverse()
    print("Case #"+str(i+1)+":", end=" ")
    for j in range(len(temp)) :
        print(temp[j],end=" ")
    print()
    
