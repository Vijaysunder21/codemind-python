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
k=0
l=0
for i in range(1,n+1):
    if(n%i==0):
        k=k+1
        if(prime(i)):
            l=l+1
print(k-l)            
        
        
        