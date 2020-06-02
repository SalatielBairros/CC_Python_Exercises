# return an integere cycle length K of a permutation. Applying a permutation K-times to a list will return the original list.
def permutation_cycle_length(permutation):
  initialArray = range(len(permutation))
  permutedArray = range(len(permutation))
  cycles = 0

  while True:
    permutedArray = [permutedArray[permutation[i]] for i in range(len(initialArray))]
    cycles += 1

    if(areEqual(initialArray, permutedArray)):
      break
  return cycles

def areEqual(first, second):
  for i in range(len(first)):
    if(first[i] != second[i]):
      return False
  return True 

print(permutation_cycle_length([4, 3, 2, 0, 1]))