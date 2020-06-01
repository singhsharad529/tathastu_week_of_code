a=int(input("Enter a number\n"))
for i in range(a+1):
    for j in range(a+1):
        if j==i or j==a-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
