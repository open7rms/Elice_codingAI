a = input()
hexa={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
for i in range(1,16) :
    print("%X"%hexa[a],"*%X"%i,"=%X"%(hexa[a]*i),sep="")
