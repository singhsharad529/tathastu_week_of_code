import math;
n=int(input("Enter a number:"))
if(n%2==0):
	print("Even")
else:
	print("Odd")
c=n;
q=0;
a=0;
while(c!=0):
	q=(q*10)+(c%10);
	a=a+math.pow(c%10,3);
	c=int(c/10);
if(n==q):
	print("Palindrome")
else:
	print("Not Palindrome")
if(n==a):
	print("Armstrong")
else:
	print("Not Armstrong")
c=0;
for i in range (2,n):
	if(n%i==0):
		c=c+1;
if(c==0):
	print("Prime")
else:
	print("Not Prime")
