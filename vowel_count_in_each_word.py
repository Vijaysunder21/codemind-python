s=input()
for i in s.split():
    c=0
    for j in i:
        if j in "aeiou":
            c=c+1
    print(c,end=" ")