c=5;
d=1;
for i in range (0,5):
	s=""
	for j in range (0,c):
		s=s+"*"
	for j in range (0,d):
		s=s+" "
	for j in range (0,c):
		s=s+"*"
	d=d+2;
	c=c-1;
	print(s)
d=d-2;
c=c+1;
for i in range (0,5):
	s=""
	for j in range (0,c):
		s=s+"*"
	for j in range (0,d):
		s=s+" "
	for j in range (0,c):
		s=s+"*"
	d=d-2;
	c=c+1;
