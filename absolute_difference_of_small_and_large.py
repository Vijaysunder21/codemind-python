s=input()
b=[]
for i in s.split():
    b.append(abs(ord(max(i))-ord(min(i))))
print(*b)