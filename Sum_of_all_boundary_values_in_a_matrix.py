r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
s=0
for i in range(r):
    for j in range(c):
        if(i==0 or j==0 or i==r-1 or j==r-1):
            s=s+m[i][j]
print(s)            
        