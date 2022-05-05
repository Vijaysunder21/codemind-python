a,b=map(int,input().split())
if(a>b):
    m=a
else:
    m=b
while(1):
    if(m%a==0 and m%b==0):
        print(m)
        break
    m=m+1
