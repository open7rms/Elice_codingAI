import sys
suncd=[]
sangcd=[]
while True :
      sun,sang = sys.stdin.readline().split()
      if int(sun)== 0 and int(sang)==0 :
            break

      for i in range(int(sun)):
            suncd.append(int(sys.stdin.readline()))

      for j in range(int(sang)):
            sangcd.append(int(sys.stdin.readline()))
      
cd=0
for same in suncd :
      low =0
      high=len(suncd)-1
      while low<=high :
            mid=int((low+high)/2)
            #if sangcd[mid] == same :
            #      print(sangcd[mid], same)
            #      cd+=1
            #      break
            if sangcd[mid] >= same :
                  high =mid-1
            else :#if sangcd[mid] < same :
                  low= mid+1
            
print(low)
