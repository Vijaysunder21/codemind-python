def pret(n):
    while(n!=0):
        d=n%10
        if(d==2 or d==3 or d==9):
            return 1
        else:
            return 0
        n=n//10
t=int(input())
c=0
for i in range(t):
    c=0
    a,b=map(int,input().split())
    for j in range(a,b+1):
        if(pret(j)):
            c=c+1
    print(c)        