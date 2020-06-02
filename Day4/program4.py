print("Enter the size of dictionary")
n = int(input())
dic={}
for i in range(n):
    key = input("Enter Key:\n")
    dic[key] = input("Enter Value:\n")

dic1 ={}
for key,value in dic.items():
    if value not in dic1.values():
        dic1[key] = value
        
print("Dictonary after removing duplicate values:\n",dic1)

 
