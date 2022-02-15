##a = input().split()
##minvalue=0

##for i in a :
##    if int(i)<minvalue :
##        minvalue=int(i)

##print(minvalue)
a,b,c =input().split()
a=int(a)
b=int(b)
c=int(c)

print((a if a<b else b) if ((a if a<b else b)<c) else c)
    
