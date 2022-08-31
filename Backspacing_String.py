s=input()
t=input()
c=[]
d=[]
for i in range(0,len(s)):
    if(s[i]=="#"):
        c.pop()
    else:
        c.append(s[i])
for i in range(0,len(t)):
    if(t[i]=="#"):
        d.pop()
    else:
        d.append(t[i])
if(str(c)==str(d)):
    print("True")
else:
    print("False")
        