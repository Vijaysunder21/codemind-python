def amic(n):
    s=0
    for i in range(1,n):
        if(n%i==0):
            s=s+i
    return s        
a=int(input())
b=int(input())
s1=amic(a)
s2=amic(b)
if(s1==b and s2==a):
    print("Amicable")
else:
    print("Not Amicable")

