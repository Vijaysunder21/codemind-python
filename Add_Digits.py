n=int(input())
s=0
while(n//10!=0):
    s=0
    while(n!=0):
        d=n%10
        s=s+d
        n=n//10
    n=s
print(s)        
    