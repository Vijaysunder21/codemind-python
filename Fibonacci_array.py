n=int(input())
arr=list(map(int,input().split()))
if(n<3):
    print("no")
else:
    f=1
    for i in range(0,len(arr)-2):
        if(arr[i]+arr[i+1]!=arr[i+2]):
            f=0
    if(f==1):
        print("yes")
    else:
        print("no")