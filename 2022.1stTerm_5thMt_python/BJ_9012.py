lineNr=int(input())
result=[]
for line in range(lineNr):
    seqs=input()#.split("")
    seqn=0
    #print(len(seqs),seqs[0])
    for seq in seqs :
        if seq =="(" :
            seqn +=1
            #print("(",seqn)
        else : 
            seqn -=1
            #print(")",seqn)

        if seqn <0 :
            break

    if seqn==0:
        result.append("YES")
    else :
        result.append("NO")
        

for index in range(len(result)) :
    print(result[index]) 