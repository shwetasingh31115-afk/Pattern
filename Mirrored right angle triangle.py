row=int(input("Enter how many rows you want:"))
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()