def pal(n):
    s=0
    temp=n
    while(n!=0):
        d=n%10
        s=s*10+d
        n=n//10
    if(s==temp):
        return 1
    else:
        return 0
n=int(input())
if(pal(n)):
    print("True")
else:
    print("False")