tuple1 = (1,2,1,4,5,8,0,3,5,7,8)
print("Tuple is :\n",tuple1)
freq = {}
for i in tuple1:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1

print("Occurence of each element in tuple:\n",freq)
