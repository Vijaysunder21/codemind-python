n=int(input())
for i in range(n):
    k=int(input())
    b=bin(k)
    l=b[2:]
    print(l.count('1'))