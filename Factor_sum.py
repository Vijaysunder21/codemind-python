def fac(n):
    s=0
    for i in range(1,n+1):
        if(n%i==0):
            s=s+i
    return s        
s=input().split(',')
k=[]
for i in s:
    k.append(int(i))
g=[]    
for i in k:
    if(fac(i) in k):
        g.append(i)
g.sort()        
if(len(g)==0):
    print("-1")
else:
    print(*g)