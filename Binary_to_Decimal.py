import math
n=int(input())
for i in range(n):
    k=input()
    l=int(k)
    i=0
    s=0
    while(l!=0):
        d=l%10
        s=s+d*pow(2,i)
        l=l//10
        i=i+1
    print(s)