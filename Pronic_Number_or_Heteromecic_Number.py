n=int(input())
f=0
for i in range(1,int(n**0.5)+1):
    if i*(i+1)==n:
        f=1
        break
if(f==1):
    print("YES")
else:
    print("NO")