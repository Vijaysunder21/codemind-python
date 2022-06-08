s=input()
s=s[::-1]
s.lower()
for i in s.split():
    k=min(i)
    if k in i and k.lower() in i:
        print(k.lower())
        break
    else:
        print(k)