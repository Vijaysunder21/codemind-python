n=int(input())
arr=list(map(int,input().split()))
k=[]
for i in arr:
    k.append(arr.count(i))
g=[]    
for i in arr:
    if(arr.count(i)==max(k)):
        g.append(i)
print(min(g))        
