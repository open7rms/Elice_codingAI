num =int(input())
ticket =input().split()
for i in range(len(ticket)) :
    ticket[i]=int(ticket[i])
ticket.sort()
for j in range(1, ticket[-1]):
    if(j not in ticket):
        print(j)
        break
