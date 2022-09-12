s=input().split(',')
a=""
for i in s:
    c=0
    i=i.split(':')
    m=i[1]
    l=i[0]
    k=list(m)
    k=sorted(k)
    for j in range(1,len(k)):
        if(int(k[-j])<=len(l)):
            n=int(k[-j])
            c=1
            break
    if(c==1):
        a=a+l[n-1]
    else:
        a=a+'X'
print(a)            

    
    