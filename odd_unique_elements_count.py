n=int(input())
arr=list(map(int,input().strip().split()))
c=0
b=[]
for i in arr:
    if i not in b:
        b.append(i)
for i in range(len(b)):
    if(b[i]%2!=0):
        c=c+1
print(c)        