s=input()
d=set(s)
k=[]
c=0
for i in d:
    k.append(s.count(i))
for i in range(1,len(k)):
    if(k[i-1]!=k[i]):
        c=c+1
if(c==0 or c==1):
    print("Valid String")
else:
    print("Not Valid")