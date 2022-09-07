s=input()
m=0
c=0
for i in range(1,len(s)):
    if(s[i-1]==s[i]):
        c=c+1
        m=max(m,c)
    else:
        c=0
print(m+1)        