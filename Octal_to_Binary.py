import math
n=int(input())
for i in range(n):
    k=input()
    l=int(k)
    s=0
    i=0
    while(l!=0):
        d=l%10
        s=s+d*pow(8,i)
        l=l//10
        i=i+1
    f=bin(s)
    print(f[2:])