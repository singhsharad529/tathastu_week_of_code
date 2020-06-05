def fabonacci(fablist):
    a = int(input('Enter a number from fabonnaci list:\n'))
    b = int(input('Enter 2nd numbr from fabonaaci list:\n'))
    c = a+b
    m=0
    if c in fablist:
        print('sum of these numbers is a fabonaaci number:\n')
        m=1
        
    
    if m==0:
          print('sum of these numbers is not a fabonaaci number:\n')



n = int(input('Enter a number to create fabonacci list:\n'))
fablist = []
a = 0
fablist.append(a)
b = 1
fablist.append(b)
c = a+b
 
for i in range(n-2):
    c=a+b
    a=b
    b=c
    fablist.append(c)

print(fablist)
fabonacci(fablist)
        
        
