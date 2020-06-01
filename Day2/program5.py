c=3;
s=""
for i in range (0,3):
	s=""
	for j in range (0,c):
		s=s+str(c)+"*"
	c=c-1;
	s=s[0:len(s)-1]
	print(s)
c=c+1;
for i in range (0,3):
	s=""
	for j in range (0,c):
		s=s+str(c)+"*"
	c=c+1;
	s=s[0:len(s)-1]
	print(s)
