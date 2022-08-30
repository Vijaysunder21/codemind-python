n=int(input())
m=[list(map(int,input().split())) for i in range(n)]
s1,s2=0,0
for i in range(n):
    for j in range(n):
        if(i==j):
            s1=s1+m[i][j]
for i in range(n):
    for j in range(n):
        if(i==(n-j-1)):
            s2=s2+m[i][j]
print("Principal Diagonal:%d"%s1)
print("Secondary Diagonal:%d"%s2)