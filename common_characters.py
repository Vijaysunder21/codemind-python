s1=input().lower().replace(" ","")
s2=input().lower().replace(" ","")
d=0
a=[]
b=[]
for i in s1:
    if i not in a:
        a.append(i)
for i in s2:
    if i not in b:
        b.append(i)
c=[]        
for i in a:
    if i in b:
        c.append(i)
        d=1
for i in b:
    if i in a:
        c.append(i)
c=list(sorted(set(c)))
if(d==0):
    print("-1")
else:    
    for i in c:
        print(i,end="")