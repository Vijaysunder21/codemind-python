def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        return 1
    else:
        return 0
n=int(input())
s=0
dc=0
if(prime(n)):
    while(n):
        d=n%10
        if(prime(d)):
            s+=1
        dc+=1
        n//=10
    if(s==dc):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
        