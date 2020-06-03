def max1(n):
    list1 = list(n)
    for i in range(len(list1)):
        list2 = list1[i:]
        list2.sort()
        list1.pop(i)
        list1.insert(i,list2[-1])
    return list1
        


n=input("Enter a Integer:\n")
lst = max1(n)

for i in lst:
    print(i,end="")




 

