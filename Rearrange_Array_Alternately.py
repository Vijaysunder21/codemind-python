n=int(input())
for i in range(n):
    k=int(input())
    a=list(map(int,input().split()))
    l=sorted(a)
    m=l[::-1]
    o=[]
    for i in range(len(l)):
        for j in range(len(m)):
            if(i==j):
                o.append(m[i])
                o.append(l[i])
    q=[]
    for i in o:
        if i not in q:
            q.append(i)
    print(*q)        
        
        