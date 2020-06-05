print('Enter the value of k:\n')
k = int(input())

n = int(input('Enter the size of the list:\n'))
print('Entet',n,'dictinct values:')
list1 = []
for i in range(n):
    list1.append(int(input()))

print('your list is :\n',list1)
if k < len(list1):
    for i in range(n):
        if k == list1[i]:               
            print('kth smallest element is :',i+1)
            break
                
      
        

else:
    print('the value of k is greater than length of list')
    
