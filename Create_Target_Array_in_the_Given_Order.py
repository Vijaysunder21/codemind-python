n=int(input())
a=list(map(int,input().split()))
k=int(input())
b=list(map(int,input().split()))
l=[]
for i in range(0,len(a)):
    l.insert(b[i],a[i])
print(*l)    