s=input()
d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
o=0
u=""
for i in range(len(s)-1):
    m=s[i]
    k=s[i+1]
    if(d[m]<d[k]):
        o=o-d[m]
    else:
        o=o+d[m]
o=o+d[s[len(s)-1]]
print(o)
    