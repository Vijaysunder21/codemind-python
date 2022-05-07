n=int(input())
c=1
temp=n
sq=n*n
while(n!=0):
    c=c*10
    n=n//10
if(sq%c==temp):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")