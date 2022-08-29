s=input().lower().split()
a=list(str(s[0]))
c=0
k=[]
for i in a:
    c1=0
    for j in range(1,len(s)):
        if i in s[j]:
            c1=c1+1
    if(c1==len(s)-1):
        c=1
        k.append(i)
if(c==0):
    print("-1")
else:
    print(min(k))
            