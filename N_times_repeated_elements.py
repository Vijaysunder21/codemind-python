n=int(input())
arr=list(map(int,input().split()))
k=int(input())
c=[]
for i in range(len(arr)):
    if arr.count(arr[i])==k:
        c.append(arr[i])
if(len(c)==0):
    print("-1")
else:        
    c=set(c)
    print(*c)
        