s=input()
b=[]
for i in s.split():
    c=0
    for j in i:
        if j in "aeiou":
            c=c+1
    b.append(c)
print(min(b))    