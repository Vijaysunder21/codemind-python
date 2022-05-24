n=int(input())
a=0
b=1
c=a+b
f=0
if(n==0 or n==1):
    print("True")
for i in range(1,n+1,1):
    c=a+b
    a=b
    b=c
    if(c==n):
        f=1
        print("True")
        break
    else:
        c=c+1
if(f==0):
    print("False")
        
        
        