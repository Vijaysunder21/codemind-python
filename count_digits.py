def dc(n):
    c=0
    if(n<0):
        n=-n
        while(n!=0):
            n=n//10
            c=c+1
        return c
    elif(n>0):
        while(n!=0):
            n=n//10
            c=c+1
        return c
    else:
        return 1
n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    print(dc(arr[i]),end=" ")
        