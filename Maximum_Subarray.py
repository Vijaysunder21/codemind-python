n=int(input())
arr=list(map(int,input().split()))
k=[]
for i in range(len(arr)):
    s=0
    for j in range(i,len(arr)):
        s=s+arr[j]
        k.append(s)
print(max(k))        