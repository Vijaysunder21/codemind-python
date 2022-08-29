r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
l=[]
for i in range(r):
    r=0
    for j in range(c):
        r+=m[i][j]
    l.append(r)
print(max(l))    
        