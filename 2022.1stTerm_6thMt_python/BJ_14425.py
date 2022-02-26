s,m =map(int,input().split())
#print(s,m)
sgroup=dict()
sum =0
for i in range(s):
    sline = input()
    sgroup[sline]=sgroup.get(sline,0)

for i in range(m) :
    mline=input()
    if mline in sgroup.keys() :
        sgroup[mline]=sgroup.get(mline,0)+1
for v in sgroup.values() :
    sum +=v
print(sum)