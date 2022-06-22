s=input()
k=[]
g=list(s)
for i in s:
    if(s.count(i)==1):
        k.append(i)
if(len(k)==len(g)):
    print("True")
else:
    print("False")
        