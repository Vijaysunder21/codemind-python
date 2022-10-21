s1,s2=map(str,input().split())
k=list(s1)
for i in s2:
    if i in k:
        k.remove(i)
if(k==[]):
    print("True")
else:
    print("False")