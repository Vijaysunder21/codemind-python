n=int(input())
s=0
k=n*n
while(k>0):
    d=k%10
    s=s+d
    k=k//10
if(s==n):
    print('Neon Number')
else:
    print('Not Neon Number')
