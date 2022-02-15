rgb =input().split()
count =0
for i in range(0,int(rgb[0])) :
    for j in range(0,int(rgb[1])) :
        for k in range(0,int(rgb[2])) :
            print(i,j,k)
            count+=1
print(count)
