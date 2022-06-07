s=input()
vc=0
cc=0
dc=0
wc=0
for i in s:
    if i in "aeiou":
        vc=vc+1
    elif i.isdigit():
        dc=dc+1
    elif i==" ":
        wc=wc+1
cc=len(s)-vc-dc-wc        
print("Vowels: %d"%vc)
print("Consonants: %d"%cc)    
print("Digits: %d"%dc)    
print("White spaces: %d"%wc)    