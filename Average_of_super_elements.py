n=int(input())
arr=list(map(int,input().split()))
m=[]
for i in arr:
    if i not in m:
        m.append(i)
c=[]
for i in m:
    if arr.count(i)==i:
        c.append(i)
if(c==[]):
    print("-1")
else:
    k=sum(c)/len(c)
    print("%.2f"%k)
        
