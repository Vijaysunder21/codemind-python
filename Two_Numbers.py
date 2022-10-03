from collections import Counter
n=int(input())
a=list(map(int,input().split()))
k=Counter(a)
for i,j in k.items():
    if(j==1):
        print(i,end=" ")