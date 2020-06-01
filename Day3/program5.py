def intersection(list1,list2):
    list3 = [value for value in list1 if value in list2]
    return list3

list1 =['Noida','Jhansi','Delhi','Mumbai','Kolkata']
list2 =['Mumbai','Ahmdabad','Goa','Noida','Chennai','Jhansi']
print("List 1:\n",list1)
print("List 2:\n",list2)
print("Intersection of both list:",intersection(list1,list2))
