r,c=map(int,input().split())
m=[list(map(int,input().split()))for i in range(r)]
maxi=0
l=0
for i in range(c):
    k=[]
    for j in range(r):
        k.append(m[j][i])
    print(max(k))        
        