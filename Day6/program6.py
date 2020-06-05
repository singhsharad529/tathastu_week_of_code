n = int(input('Enter the size of the array:\n'))
print('Enter ',n,'number in an array:\n')
array = []
for i in range(n):
    array.append(int(input()))

print('array is created sucessfully!!')
sortedarray = []
sortedarray = array.copy()
rotatedarray = array.copy()
 

sortedarray.sort()
 
 
print(array)
print(sortedarray)

temp = rotatedarray[0]
for i in range(n-1):
    rotatedarray[i]=rotatedarray[i+1]
    
rotatedarray[n-1]=temp

print(rotatedarray)


if array==sortedarray:
    print('list is sorted')
if array==rotatedarray:
    print('list is roatated')
