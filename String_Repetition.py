s=input()
n=int(input())
m=s.count('a')
k=n//len(s)
j=s[:(n%len(s))]
print(k*m + j.count('a'))