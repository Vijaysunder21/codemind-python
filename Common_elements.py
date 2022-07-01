a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
c=[]
d=[]
for i in range(len(arr)):
    for j in range(len(brr)):
        if(arr[i]==brr[j]):
            c.append(brr[j])
for i in range(len(arr)):
    for j in range(len(brr)):
        if(arr[i]==brr[j]):
            d.append(arr[i])
e=[]
for i in c:
    if i not in e:
        e.append(i)
print(*e)        
            