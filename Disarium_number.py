n=int(input())
c=0
s=0
temp=n
while(temp!=0):
    temp=temp//10
    c=c+1
temp=n
while(temp!=0):
    d=temp%10
    s=s+pow(d,c)
    temp=temp//10
    c=c-1
if(s==n):
    print("True")
else:
    print("False")
    