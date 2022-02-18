BookNr = int(input())
BookList=dict()

for index  in range(BookNr) :
    BookName=input()
    BookList[BookName] = BookList.get(BookName,0)+1

MaxNum=list(BookList.values())
MaxNum.sort(reverse=True)
#print(MaxNum)
Books=[]
for k,v in BookList.items() :
    if MaxNum[0] ==v :
        Books.append(k)
Books.sort()
print(Books)
