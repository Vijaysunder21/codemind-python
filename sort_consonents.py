s=input().split()
x=[]
for i in s:
    j=str(i)
    c=[]
    d=""
    for k in j:
        if k not in "AEIOUaeiou":
            c.append(k)
    c.sort()
    m=0
    for k in j:
        if k not in "AEIOUaeiou":
            d=d+c[m]
            m=m+1
        else:
            d=d+k
    x.append(d)
print(" ".join(x))    
    