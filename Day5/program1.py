def modify(n):
    lst=[]
    print("Enter ",n," Integers:")
    for i in range(n):
        lst.append(int(input()))
        if(lst[i]==0):
            lst[i]=5
    return lst


n = int(input("Enter number of Integer to Input\n"))
print("after replacing 0 with 5:",modify(n))
    
    
