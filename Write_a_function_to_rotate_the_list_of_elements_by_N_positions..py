n=int(input())
arr=list(map(int,input().split()))
k=int(input())
for i in range(0,k):
    m=arr[len(arr)-1]
    for j in range(len(arr)-1,-1,-1):
        arr[j]=arr[j-1]
    arr[0]=m;
print(*arr)    