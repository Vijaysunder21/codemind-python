n=int(input())
a=list(map(str,input().split()))
c=[]
for i in range(n):
    c.append(len(a[i]))
k=max(c)
g=0
for i in range(n):
    if(len(a[i])==k):
        print(a[i],end=" ")