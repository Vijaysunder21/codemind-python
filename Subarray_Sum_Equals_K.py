a,b=map(int,input().split())
arr=list(map(int,input().split()))
c=0
for i in range(len(arr)):
    s=0
    for j in range(i,len(arr)):
        s=s+arr[j]
        if(s==b):
            c=c+1
print(c)        