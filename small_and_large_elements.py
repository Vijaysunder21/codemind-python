s=input()
l=[]
for i in s.split():
    print(min(i),end=" ")
    break
for i in s[::-1].split():
    print(max(i),end=" ")
    break
    