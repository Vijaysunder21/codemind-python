def rev(n):
    s=0
    while(n!=0):
        d=n%10
        s=s*10+d
        n=n//10
    return s    
n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    print(rev(arr[i]),end=" ")