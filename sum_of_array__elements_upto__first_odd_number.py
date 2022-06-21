n=int(input())
arr=list(map(int,input().strip().split()))
s=0
for i in range(len(arr)):
    if(arr[i]%2==0):
        s=s+arr[i]
    elif(arr[i]%2==1):
        break
print(s)    