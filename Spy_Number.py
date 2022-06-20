n=int(input())
k=list(str(n))
s=0
p=1
for i in range(len(k)):
    s=s+int(k[i])
    p=p*int(k[i])
if(s==p):
    print("Spy Number")
else:
    print("Not Spy Number")
    
    