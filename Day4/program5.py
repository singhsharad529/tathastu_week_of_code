size = int(input("Enter the number of votes :\n"))

v = []
for i in range(size):
    vote = input("Enter Candidate\n")
    v.append(vote)

v.sort()

print(v)

candidate = {}
for i in v:
    if i in candidate:
        candidate[i] += 1
    else:
        candidate[i] = 1

max1 = 0
for i in candidate:
    if candidate[i]>max1:
        max1 = candidate[i]

for i in candidate:
    if candidate[i] == max1:
        print("Maximum vote gain by candidate: ",i,"with votes: ",max1)


    
