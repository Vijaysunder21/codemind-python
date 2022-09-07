n=int(input())
for i in range(n):
    s=input()
    c=0
    for j in range(1,len(s)):
        if(s[j-1]==s[j]):
            c=c+1
    print(c)        