n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if(sum(a)-sum(b))<0:
    print(abs(sum(a)-sum(b)))
else:
    print(0)