import sys
trees=dict()
count=0


#names=.readlines().rstrip('\n')
for name in sys.stdin:
    if name=='\n':
        break
    name=name.rstrip()
    trees[name]=trees.get(name,0)+1
    count+=1
text=''
output=[]
for k,v in trees.items() :
    text = "{} {:.4f}"
    output.append(text.format(k,v/count*100))
output.sort()
#print(output)
for i in range(len(output)) :
    print(output[i])