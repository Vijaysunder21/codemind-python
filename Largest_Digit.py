k=int(input())
l=k%10
k=k//10
m=k%10
k=k//10
n=k%10
k=k//10
o=k%10
k=k//10
if(o>l and o>m and o>n):
    print(o)
elif(n>l and n>m and n>o):
    print(n)
elif(m>l and m>n and m>o):
    print(m)
else:
    print(l)
