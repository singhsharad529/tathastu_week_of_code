n=int(input("enter the size of the list:\n"))
print('Enter ',n,'values in the list:')
list1=[]
for i in range(n):
    list1.append(int(input()))

max = 3*list1[0]
for i in range(1,n):
    if max<3*list1[i]:
        max=3*list1[i]
list1.sort()
maximum=1
for i in range(n-1,n-4,-1):
    maximum *= list1[i]

print('Highest product possible by multiplying 3 numbers :',maximum)


 
