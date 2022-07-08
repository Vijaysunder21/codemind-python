s=input()
k=s[::-1]
c=0
for i in range(0,len(s)//2):
    if(s[i] in "aeiouAEIOU" and k[i] not in "aeiouAEIOU" and s[i]!=" " and k[i]!=" "):
        c=c+1
for i in range(0,len(s)//2):
    if(s[i] not in "aeiouAEIOU" and k[i] in "aeiouAEIOU" and s[i]!=" " and k[i]!=" "):
        c=c+1
print(c)        