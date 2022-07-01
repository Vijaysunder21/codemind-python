a,b=map(int,input().split())
arr=list(map(int,input().split()))
c=0
for i in range(len(arr)):
    if(arr[i]%b==0):
        c=c+1
print(c)