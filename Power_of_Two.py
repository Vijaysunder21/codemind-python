import math
n=int(input())
k=2
if(n<=0):
    print("False")
elif(n==1):
    print("True")
else:
    i=0
    while(k<=n):
        k=2
        k=k**i
        if(k==n):
            print("True")
            quit()
        i=i+1
    print("False")