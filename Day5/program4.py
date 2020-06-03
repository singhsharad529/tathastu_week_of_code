def knapsack(values,weight,maxWeight):
    sumWeight=0
    sumValues=0
    values.sort()
    weight.sort()
    i=0
    while(sumWeight+weight[i]<=maxWeight):
        sumValues+=values[i]
        sumWeight+=weight[i]
        i+=1
    print("Maximum value knapsack can take is",sumValues)
n=int(input("Enter the number of items"))
print("Enter the values of items")
values=[]
weight=[]
for i in range(n):
    values.append(int(input()))
print("Enter the Weight of items")
for i in range(n):
    weight.append(int(input()))
W=int(input("Enter the maximum weight knapsack could hold "))
knapsack(values,weight,W)
