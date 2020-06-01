r=[]

print("Enter elements: ")
l = [int(x) for x in input().split()]
n = min(l)
s(l)
sumList = list(set(r))

while 1:
    if n not in sumList:
        print("the least integer is: ", n)
        break
    n +=1

def s(l,s=0):
    for i in l:
        r.append(s+i)
        l1=list(l)
        l1.remove(i)
        s(l1,s+i)
