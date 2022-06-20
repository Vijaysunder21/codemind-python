def iself(i):
    c=0
    dc=0
    n=i
    while(i):
        d=i%10
        if(d==0):
            return 0
        if(n%d==0):
            c+=1
        dc+=1
        i=i//10
    if(c==dc):
        return 1
    else:
        return 0
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(iself(i)):
        print(i,end=' ')