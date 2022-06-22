s=input()
k=input()
f=0
for i in s:
    if i==k:
        f=1
        print("True")
        print(s.index(i))
        break
if(f==0):
    print("False")
    