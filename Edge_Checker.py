a,b=map(int,input().split())
l=max(a,b)
c=abs(a-b)
if(c==1 or c==-1):
    print("Yes")
elif(l==10 and c==9 or c==-9):
    print("Yes")
else:
    print("No")