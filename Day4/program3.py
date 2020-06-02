print("Enter the sizes of different person with their name:\nEnter number of person:")
n = int(input())
dic={}
for i in range(n):
    key = input("Enter Name:\n")
    dic[key] = int(input("Enter the size:\n"))

max1 = max(dic.values())
max2 = 0
for i in dic.values():
    if(i>max2 and i<max1):
        max2 = i

print("Second maximum values in sizes:\n",max2)
