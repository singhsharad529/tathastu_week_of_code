a=input('Enter a String\n')
new=''
for i in a:
    if i not in new:
        new=new+i
print("String after removing of duplicate charactesr:\n",new)
