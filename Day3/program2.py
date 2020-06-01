
from itertools import permutations   
def allPermutations(str):  
     permList = permutations(str)
     print("All Permutation")
     for perm in list(permList): 
         print (''.join(perm))


str = input('Enter a String\n')
allPermutations(str) 
