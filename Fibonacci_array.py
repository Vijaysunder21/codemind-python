n=int(input())
arr=list(map(int,input().split()))
if(n<3):
    print("no")
else:
    for i in range(2,len(arr)):
        if(arr[i]!=arr[i-1]+arr[i-2]):
            print("no")
            quit()
    print("yes")