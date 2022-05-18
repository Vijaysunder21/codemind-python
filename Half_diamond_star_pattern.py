n=int(input())
if(n<=2 or n>100):
    print("The pattern is not possible")
    quit()
for i in range(1,n+1):        
    for j in range(1,i+1):
        print('*',end="")
    print()
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print('*',end="")
    print()    