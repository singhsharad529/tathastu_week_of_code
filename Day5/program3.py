def stole(listhouse):
    maxvalue = 0
    for i in range(0,len(listhouse),2):
        maxvalue += listhouse[i]
    return maxvalue


n = int(input("Enter the number of house:\n"))
print("Enter ",n,"values")
listhouse = []
for i in range(n):
    listhouse.append(float(input()))

print("Maximum value stolen by from house:\n",stole(listhouse))
        
