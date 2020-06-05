n=int(input('Enter the size of the array:\n'))
print('Enter ',n,'values for the array:\n')
arr =[]
for i in range(n):
    arr.append(int(input()))


for i in range(n):
    number = arr[i]
    left_count = i
    right_count = n-i-1
    left = 0
    right = 0
    for j in range(left_count):
        if arr[j]<number:
            left += 1
    
    for j in range(i+1,n):
        if arr[j]>number:
            right += 1
    if left==left_count and right==right_count:
        print('Number is :\n',number)
        break
