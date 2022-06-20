n=int(input())
s=0
d=0
if(n<0):
    n=-n
    while(n):
        d=n%10
        s=s*10+d
        n=n//10
    print(-s)
else:
    while(n):
        d=n%10
        s=s*10+d
        n=n//10
    print(s)    
    
    
        