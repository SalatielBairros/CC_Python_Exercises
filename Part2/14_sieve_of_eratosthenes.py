def seed(n):
    if(n > 2):
        array = [True] * (n + 1)
        array[0] = False
        array[1] = False
        return array
    return [False, False, True]


def sieve_of_eratosthenes(n):
    if(n == 2):
      return [2]
    elif(n < 2 ):
      return []
    
    control = seed(n)
    
    for i in range(len(control))[2::]:
      for p in range(len(control))[(i + 1)::]:
        if((p % i) == 0):
          control[p] = False

    response = list()
    for c in range(len(control)):
      if(control[c]):
        response.append(c)
    
    return response

print(sieve_of_eratosthenes(100))
