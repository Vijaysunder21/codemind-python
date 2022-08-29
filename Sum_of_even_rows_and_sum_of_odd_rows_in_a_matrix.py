r,c=map(int,input().split())
s1,s2=0,0
for i in range(r):
    a=list(map(int,input().split()))
    if(i%2==0):
        s1+=sum(a)
    else:
        s2+=sum(a)
print(s1,s2)