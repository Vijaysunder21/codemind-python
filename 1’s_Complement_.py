n=int(input())
f=bin(n)
l=f[2:]
q=""
for i in l:
    if i=='1':
        q=q+'0'
    elif(i=='0'):
        q=q+'1'
print(int(q,2))