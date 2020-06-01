  
n=int(input("Enter the value of n:"))
a,b=0,1
c=0;
print(a)
print(b)
for i in range (1,n-1):
	c=a+b;
	a=b;
	b=c;
	print(c)
