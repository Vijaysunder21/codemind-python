n=int(input())
arr=list(map(int,input().strip().split()))
arr=sorted(set(arr))
l=len(arr)
if(n==2):
    print(max(arr))
else:
    print(arr[l-3])