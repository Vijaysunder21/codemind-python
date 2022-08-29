r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
s=0
for i in range(r):
    for j in range(c):
        if(i==j):
            s=s+m[i][j]
        elif(i==(r-j-1)):
            s=s+m[i][j]
print(s)            
        