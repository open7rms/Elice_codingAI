import sys

input = sys.stdin.readline
n = int(input())
x=dict()
y=dict()

for i in range(n) :
      a,b=input().split()
      x[a]=x.get(a,0)+1
      y[b]=y.get(b,0)+1
answerx=0
for xv in x.values() :
      answerx=answerx+xv*(xv-1)*0.5

answery=0
for yv in y.values() :
      answery=answery+yv*(yv-1)*0.5

print(int(answerx)+int(answery))
