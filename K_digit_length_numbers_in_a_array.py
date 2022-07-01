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
a,b=map(int,input().split())
arr=list(map(int,input().split()))
c=0
for i in range(a):
    if(dc(arr[i])==b):
        c=c+1
print(c)        