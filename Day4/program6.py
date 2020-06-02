print("enter list of words: ")
dic = [x for x in input().split()]
print("enter list of letters:")
arr = [x for x in input().split()]

count = {}
for i in arr:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

print()

for i in dic:
    s = ""
    count1=dict(count)
    for j in i:
        if j in count1 and count1[j]>0:
            s=s+j
            count1[j]-=1
    if s==i:
        print(i) 
