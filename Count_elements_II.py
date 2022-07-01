a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
c=[]
d=[]
for i in arr:
    if i not in brr:
        c.append(i)
for i in brr:
    if i not in arr:
        d.append(i)
e=[]
print(len(set(c+d)))
        
            