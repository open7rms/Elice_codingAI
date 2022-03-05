from itertools import count


numL=int(input())
op=input()

def sum(a,b) :
    return a+b

def minus(a,b) :
    return a-b

def mul(a,b) :
    return a*b

def div(a,b):
    return a/b

number=dict()
num=[]
count=0
for i in range(numL):
    number[chr(65+i)]=int(input())

for i in op :
    if ord(i)>=65 and ord(i)<=90 :
        num.append(number[i])
        
        #print(num)
    elif i=="+" :
        a=num.pop()
        b=num.pop()
        #print("+",sum(a,b))
        num.append(sum(a,b))
    elif i=="-":
        a=num.pop()
        b=num.pop()
        #print("-",minus(b,a))
        num.append(minus(b,a))
    elif i=="*":
        a=num.pop()
        b=num.pop()
        #print("*",mul(a,b))
        num.append(mul(a,b))
    elif i=="/":
        a=num.pop()
        b=num.pop()
        #print("/",div(b,a))
        num.append(div(b,a))

print('%.2f' %num[0])