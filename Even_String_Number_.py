s=input()
k=[]
for i in s:
    if i.isdigit():
        k.append(i)
c=0
for i in k:
    if(int(i)%2==0):
        c=c+1
if(c==0):
    print("-1")
else:
    l=set(k)
    l=sorted(l)
    m,f,v=[],[],0
    for i in range(len(l)):
        if(int(l[i])%2==0 and v==0):
            m.append(l[i])
            v=v+1
        else:
            f.append(l[i])
    print("".join(f[::-1])+"".join(m))
            
    