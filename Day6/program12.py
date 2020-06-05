n=int(input("Enter the number of Strings you want to enter:"))
 
arr=[]
 
for i in range(n):
    arr.append(input("Enter your String:"))
m = len(arr)
if (m == 0):
    print("no string in a array")
elif (m == 1):
    print(arr[0])
arr.sort()
minimum = min(len(arr[0]), len(arr[m - 1]))
 
i=0
while i<minimum:
    if arr[0][i] == arr[n - 1][i]:
        i += 1
    else:
        break
print("longest prefix is:",arr[0][0: i] )
