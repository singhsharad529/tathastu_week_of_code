def rotatation(lis,n):
    for i in range(n//2):
        for j in range(i,n-1-i):
            temp = lis[i][j]
            lis[i][j] = lis[n - 1 - j][i]
            lis[n - 1 - j][i] = lis[n - 1 - i][n - 1 - j]
            lis[n - 1 - i][n - 1 - j] = lis[j][n - 1 - i]
            lis[j][n - 1 - i] = temp

    print("Matrix after roatation:\n")
    for i in range(n):
        for j in range(n):
            print("{0:<4d}".format(lis[i][j]),end=" ")
        print()

list=[]
n=int(input("enter dimension of matrix :\n"))
num=1
for i in range(n):
    a=[]
    for i in range(n):
        a.append(num)
        num+=1
    list.append(a)
print("normal matrix representation:")
for i in range(n):
    for j in range(n):
        print("{0:<4d}".format(list[i][j]),end=" ")
    print()
rotatation(list,n)
