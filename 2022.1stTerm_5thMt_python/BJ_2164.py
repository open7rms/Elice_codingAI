import sys
from collections import deque
Nr = int(sys.stdin.readline())
#1cardDeck=deque([])
cardDeck=deque([int(x) for x in range(1,Nr+1)])
#print(cardDeck)
while (len(cardDeck)>0):
    if len(cardDeck)==1 :
        print(cardDeck[0])
        break
    else:
        cardDeck.popleft()
        last=cardDeck.popleft()
        #cardDeck=cardDeck[1:]
        cardDeck.append(last)
        print(cardDeck)