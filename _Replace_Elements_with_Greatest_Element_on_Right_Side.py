n=int(input())
a=list(map(int,input().split()))
k=[]
for i in range(0,len(a)):
    if(i==n-1):
        k.append(-1)
        break
    d=a[i+1:n]
    k.append(max(d))
print(*k)        
        