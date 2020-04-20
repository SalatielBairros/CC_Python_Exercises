
# indices is a list of integers.
# All elements of indices are within the bounds of the list indices

# This function should return a list of cycles.


def cycles(indices):
    cycles = []
    currentCycle = []
    visited = []
    currentItem = indices[0]

    while True:
      while currentItem not in currentCycle:
          visited.append(currentItem)
          currentCycle.append(currentItem)
          currentItem = indices[currentItem]

      cycles.append(currentCycle)
      currentCycle = []

      notVisited = [i for i in indices if i not in visited]

      if(len(notVisited) == 0):
        break

      currentItem = notVisited[0]

    return cycles

print(cycles([2, 0, 1, 4, 3, 5]))
print(cycles([0, 1, 2, 3]))
print(cycles([3, 2, 0, 1]))