s=input()
l=input()
c=0
for i in s.split():
    for j in l.split():
        if i.lower()==j.lower():
            c=c+1
print(c)            
            