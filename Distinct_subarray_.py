l=int(input())
r=int(input())
k=[]
c=0
for i in range(l,r+1):
    k.append(i)
for i in range(len(k)):
    s=0
    for j in range(i,len(k)):
        s=s+k[j]
        if(s%2==1):
            c=c+1
print(c)            