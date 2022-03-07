le,position=4,2#map(int,input().split())

nums=[1,2,3,4]#list(map(int,input().split()))
count=1
num=0
print(type(max(nums)))
while(True) :
    #num=nums[0]
    nums.pop()
    print(num)
    if num == max(nums) :
        if position ==0 :
            print(count)
            break
        else :
            #nums.pop(0)
            position -=1
            count +=1
    else :
        #num=nums.pop(0)
        nums=nums.append(num)
        if position ==0 :
            position = len(nums)
        else :
            position -=1