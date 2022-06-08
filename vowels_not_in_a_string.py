s=input()
v=list("aeiou")
b=[]
for i in s:
    if i in "aeiou":
        b.append(i)
for i in v:
    if i not in b:
        print(i,end=" ")
b=set(b)
if(len(b)==len(v)):
    print("0")
        