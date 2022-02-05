import sys

input = sys.stdin.readline
actions=[]
while len(actions)<=24 :
      actions=actions+input().split()
actions=actions[:24]
actcount={"Re" : 0,
          "Pt" : 0,
          "Cc" : 0,
          "Ea" : 0,
          "Tb" : 0,
          "Cm" : 0,
          "Ex" : 0}
for action in actions :
      actcount[action]=actcount.get(action,0)+1

for k,v in actcount.items() :
      print(k,v,round(v/24,2))
      if(k == "Ex"):
            break
print("Total 24 1.00")


      


