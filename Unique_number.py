n=int(input())
k=list(str(n))
g=len(k)
k=set(k)
s=len(k)
if(g==s):
    print("Unique Number")
else:
    print("Not Unique Number")
