n=int(input())
arr=list(map(int,input().split()))
c=0
m=0
for i in arr:
    if(i==1):
        c=c+1
        m=max(m,c)
    else:
        c=0
print(m)        