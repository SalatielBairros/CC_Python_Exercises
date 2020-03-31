array = list()
calleds = list()

def list_jumps(jumps):
    global array
    global calleds
    array = jumps

    #workaround for the udemy bug
    calleds = []
    return jump(0)


def jump(index):
    global array
    global calleds    

    maxIndex = len(array) - 1

    if(0 <= index <= maxIndex):
      if(index in calleds):
        return 'cycle'

      calleds.append(index)
      value = array[index]
      next = index + value
      return jump(next)
    else:
        return 'out-of-bounds'


print(list_jumps([1]))
