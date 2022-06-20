n=int(input())
k=n*n
l=list(str(k))
s=0
for i in range(len(l)):
    s=s+int(l[i])
if(s==n):
    print("Neon Number")
else:
    print("Not Neon Number")