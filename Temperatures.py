n=int(input())
arr=list(map(int,input().split()))
k=[]
for i in range(0,len(arr)-1):
    c=0
    for j in range(i+1,len(arr)):
        if(arr[i]<arr[j]):
            c=c+1
            k.append(c)
            break
        else:
            c=c+1
    if not arr[i]<arr[j]:
        k.append(0)
k.append(0)
print(*k)