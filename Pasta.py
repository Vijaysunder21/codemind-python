n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(m):
    if b[i] in a:
        c.append(b[i])
if(len(set(c))==m):
    print("Yes")
else:
    print("No")
        
        