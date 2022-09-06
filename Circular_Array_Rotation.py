n,k,q=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(0,k):
    m=arr[len(arr)-1]
    for j in range(len(arr)-1,-1,-1):
        arr[j]=arr[j-1]
    arr[0]=m;
for i in range(q):
    l=int(input())
    print(arr[l])