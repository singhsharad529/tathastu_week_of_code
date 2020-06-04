n = int(input('Enter the size of the List which contains o and 1 only:\n'))
lst = []
for i in range(n):
    a = int(input())
    lst.append(a)


print("your list:\n",lst)
count=0;
for i in lst:
    if i>=0 and i<=1:
        count +=1       
    else:
        print('You have enter number which is not 0 and 1 plese start again:\n')
        break
        
lst.sort(reverse = True)
if(count==n):
    print("sorted List:\n",lst)
              
