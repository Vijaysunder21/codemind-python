n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    k=0
    f=0
    for i in range(0,1000000):
        if((i*i)%b==a):
            print(i)
            f=1
            break
    if(f==0):
        print("-1")