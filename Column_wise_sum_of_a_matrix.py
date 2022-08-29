r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
for i in range(c):
    c=0
    for j in range(r):
        c+=m[j][i]
    print(c,end=" ")
        