def gcd(a,b):
    if a>b:
        s=b
    else:
        s=a
    for i in range(1,s+1):
        if(a%i==0 and b%i==0):
            h=i
    return h
a,b=map(int,input().split())
print(gcd(a,b))
