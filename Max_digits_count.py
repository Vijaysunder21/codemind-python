n=int(input())
a=list(map(str,input().split()))
k=len(max(a))
c=0
for i in range(n):
    if(len(a[i])==k):
        c=c+1
print(c)        