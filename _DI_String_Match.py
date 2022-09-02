s=input()
a=[]
m,n=0,len(s)
for i in s:
    if i=="I":
        a.append(m)
        m=m+1
    elif i=="D":
        a.append(n)
        n=n-1
a.append(m)    
print(*a)        
        