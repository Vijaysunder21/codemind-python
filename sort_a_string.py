s=input()
x=[]
for i in s:
    if i.isalnum():
        x.append(i)
x.sort()
m=0
for i in s:
    if i.isalnum():
        print(x[m],end="")
        m=m+1
    else:
        print(i,end="")