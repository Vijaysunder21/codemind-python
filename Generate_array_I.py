n=int(input())
arr=list(map(int,input().split()))
for i in range(0,len(arr)-1,2):
    for j in range(arr[i+1]):
        print(arr[i],end=" ")