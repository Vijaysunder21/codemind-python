n=int(input())
arr=list(map(int,input().split()))
a=[]
for i in arr:
    if arr.count(i)>=2:
        a.append(i)
g=0        
k=set(a)
for i in k:
    if(a.count(i)%2==0):
        g=g+a.count(i)//2
    else:
        g=g+a.count(i)//2
print(g)        
        