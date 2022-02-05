
n =int(input())
k =int(input())
numin=[]
for i in range(n):
      numin.append(input())

nums=dict()
if k==2 :
      for i in range(n):
           for j in range(n):
                 if i !=j:
                       nums[numin[i]+numin[j]]=nums.get(numin[i]+numin[j],0)+1
elif k==3 :
      for i in range(n):
           for j in range(n):
                 for k in range(n):
                       if (i !=j) and (i !=k) and(j !=k):
                             nums[numin[i]+numin[j]+numin[k]]=nums.get(numin[i]+numin[j]+numin[k],0)+1
elif k==4 :
      for i in range(n):
           for j in range(n):
                 for k in range(n):
                        for l in range(n):
                             if (i !=j) and (i !=k) and(i !=l) and (j !=k) and (j !=l) and (k !=l):
                                   nums[numin[i]+numin[j]+numin[k]+numin[l]]=nums.get(numin[i]+numin[j]+numin[k]+numin[l],0)+1

print(len(nums.keys()))
