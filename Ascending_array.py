n=int(input())
arr=list(map(int,input().split()))
if(arr==sorted(set(arr))):
    print("yes")
else:
    print("no")