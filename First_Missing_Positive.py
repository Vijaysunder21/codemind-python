n=int(input())
a=list(map(int,input().split()))
k=[]
if(min(a)==0):
    print(max(a)+1)
elif(min(a)>1):
    print(1)
else:
    for i in range(1,max(a)):
        k.append(i)
    for i in k:
        if i not in a:
            print(i)
            break