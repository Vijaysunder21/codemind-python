n=int(input())
for i in range(n):
    k=0
    s=input()
    for i in s:
        if i.isdigit():
            k=k+1
    if(k==len(s)):
        print("True")
    else:
        print("False")