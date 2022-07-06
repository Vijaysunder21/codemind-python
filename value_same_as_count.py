n=int(input())
arr=list(map(int,input().split()))
m=set(arr)
c=0
for i in m:
    if arr.count(i)==i:
        c=c+1
print(c)        
        
