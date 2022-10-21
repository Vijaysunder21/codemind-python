n=int(input())
a=list(map(int,input().split()))
k=min(a)
c=0
for i in range(1,k+1):
    c=0
    for j in range(len(a)):
        if(a[j]%i==0):
            c=c+1
    if(c==len(a)):
        h=i
print(h)