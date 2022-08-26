n=int(input())
arr=list(map(int,input().split()))
a=0
b=0
for i in range(0,n-2,2):
    if(arr[i]<arr[i+1] and arr[i+1]>arr[i+2]):
        a=a+1
    elif(arr[i]>arr[i+1] and arr[i+1]<arr[i+2]):
        a=a+1
    else:
        b=1
if(b==0):
    print("yes")
else:
    print("no")
        