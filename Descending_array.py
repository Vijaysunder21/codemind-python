n=int(input())
arr=list(map(int,input().split()))
k=sorted(arr)
if(arr==k[::-1]):
    print("yes")
else:
    print("no")