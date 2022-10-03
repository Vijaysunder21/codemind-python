from collections import Counter
n=int(input())
arr=list(map(int,input().split()))
k=Counter(arr)
for i,j in k.items():
    if(j==1):
        print(i)