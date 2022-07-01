def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        return 1
    else:
        return 0
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
c=[]
d=0
for i in range(len(arr)):
    if(prime(arr[i])):
        c.append(arr[i])
for i in range(len(c)):
    if(c[i]>=k):
        d=d+1     
print(d)        