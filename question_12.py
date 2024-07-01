def findcount(arr,num,diff):
    count=0
    for i in arr:
        if(abs(num-i)<=diff):
            count+=1
        if count==0:
            return -1
    return count
arr=list(map(int,input().split()))
num=int(input())
diff=int(input())
print(findcount(arr,num,diff))