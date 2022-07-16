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
k=arr.index(min(arr))
g=arr.index(max(arr))
if k>g:
    k,g=g,k
c=0
for i in range(k,g+1):
    if(prime(arr[i]                                                                                 )):
        c=c+1
print(c)        
