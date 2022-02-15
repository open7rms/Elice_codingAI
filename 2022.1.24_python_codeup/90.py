a,m,d,n = input().split()
seq=[int(a)]
for i in range(0,int(n)) : 
    seq.append(seq[i]*int(m)+int(d))
print(seq[int(n)-1])
