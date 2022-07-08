n=int(input())
a=list(map(str,input().split()))
c=[]
for i in range(n):
    c.append(len(a[i]))
k=min(c)
g=0
for i in range(n):
    if(len(a[i])==k):
        g=g+1
print(g)        