from operator import itemgetter 
n = int(input('Enter the size of the array:\n'))
list1=[]
for i in range(n):
    list1.append(int(input()))
list1.sort()
print(list1)
smallest = 0
 
for i in range(1,n):
    var1 = itemgetter(i)(list1)
    var2 = itemgetter(i-1)(list1)
    if ((var1-1)!=var2):
        smallest = var1-1
        break


print('smallest value is:\n',smallest)
 
 
        
        
