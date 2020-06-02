size=int(input("enter size of list: "))
l=[]
for i in range(size):
    l.append(tuple(input("enter comma sperated tuple elements: ").split(",")))

n = int(input("enter the index for sorting: "))

l.sort(key=lambda x:x[n])

print("sorted list is: ",l)
