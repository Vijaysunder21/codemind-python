a=int(input())
arr=list(map(int,input().strip().split()))
b=int(input())
brr=list(map(int,input().strip().split()))
k=int(input())
c=0
for i in range(a):
    if k>=arr[i] and k<=brr[i]:
        c=c+1
print(c)        
    
        
    
