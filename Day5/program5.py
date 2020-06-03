def letsort(list1):
    evenlist=[]
    for i in range(len(list1)):
        ele = list1[i]
        if(ele%2 == 0):
            evenlist.append(list1[i])
            list1.pop(i)
    list1.sort()
    evenlist.sort()
    evenlist.reverse()
    
    print("The final list after sorting is")
    print(lst)
    print(evenlist)
    
n=int(input("Enter the size of the list:\n"))
print("Enter",n,"tems of list")
list1=[]
for i in range(n):
    list1.append(int(input()))

letsort(list1)
