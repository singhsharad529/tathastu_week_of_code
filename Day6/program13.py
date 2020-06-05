  
n=int(input("size of array:"))
arr=[]
print("plz enter real numbers in this array:\n example- 0.3")
for i in range(n):
    arr.append(input("enter real numbers greater than  zero:"))
 print(arr)
arr2=list(arr)
arr3=[]
for a in arr2:
    arr2.remove(a)
    for b in arr2:
        arr2.remove(b)
        for c in arr2:
            if float(float(a)+float(b)+float(c))<2 and float(float(a)+float(b)+float(c))>1:
                if float(a)+float(b)+float(c) not in arr3:
                    print("triplet found a=",a,"b=",b,"c=",c,"\na+b+c=",float(a)+float(b)+float(c),"\n")
                    arr3.append(float(a)+float(b)+float(c))
        arr2.append(b)
    arr2.append(a)
