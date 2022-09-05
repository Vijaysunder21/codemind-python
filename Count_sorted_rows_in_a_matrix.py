r,c=map(int,input().split())
d=0
for i in range(r):
    m=list(map(int,input().split()))
    if(m==sorted(m) or m[::-1]==sorted(m)):
        d=d+1
print(d)        
        
    