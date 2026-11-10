rowsize=int(input("Enter the number of rows:"))
if rowsize%2==0:
    halfdirow=int(rowsize/2)
else:
    halfdirow=int(rowsize/2)+1
space=halfdirow-1
for i in range(1,halfdirow+1):
    for j in range(1,space+1):
        print(end=" ")
    space=space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
        num+=1
    print()
space=1
for i in range(1,halfdirow):
    for j in range(1,space+1):
        print(end=" ")
    space+=1
    num=1
    for j in range(1,2*(halfdirow-i)):
        print(end=str(num))
        num+=1
    print()