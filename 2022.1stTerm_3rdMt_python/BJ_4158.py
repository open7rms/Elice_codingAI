import sys

input = sys.stdin.readline
sun,sang = input().split()
suncd=[]
sangcd=[]
for i in range(int(sun)):
      suncd.append(int(input()))

for j in range(int(sang)):
      sangcd.append(int(input()))

sun,sang = input().split()

cd=0
for same in suncd:
      if same in sangcd :
            cd =cd+1

print(cd)
