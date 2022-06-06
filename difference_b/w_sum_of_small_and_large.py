s=input()
b=[]
c=[]
for i in s.split():
    b.append(ord(max(i)))
for i in s.split() :
    c.append(ord(min(i)))
s1=0
s2=0
for i in range(len(b)):
    s1=s1+b[i]
for i in range(len(c)):
    s2=s2+c[i]
print(abs(s1-s2))    