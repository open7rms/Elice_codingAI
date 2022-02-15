n=int(input())
matrix=[[0 for column in range(19)] for row in range(19)]
for i in range(n):
    a,b =input().split()
    matrix[int(a)-1][int(b)-1]=1

for i in range(19):
    for j in range(19):
        print(matrix[i][j],end=" ")
    print()
    

