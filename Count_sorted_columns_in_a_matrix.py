r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
k=0
for i in range(c):
    d=[]
    for j in range(r):
        d.append(m[j][i])
    if(d==sorted(d) or d[::-1]==sorted(d)):
        k=k+1
print(k)        
        
    
        