n=int(input("enter the value of n equal to number of sorted array:"))
list1=[]
for i in range(n):
    small=[]
    m=int(input("enter the size of array:"))
    for j in range(m):
        small.append(int(input("enter elements in your array")))
    small.sort()
    list1.append(small)
print(list1)

a=[]
for i in range(n):
    print(list1[i])
    a.extend(list1[i])
a.sort()
print(a)
