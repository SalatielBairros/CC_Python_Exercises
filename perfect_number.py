def perfect(number):

  if(number < 0):
    return False

  sum = 0
  counter = 1
  while (counter < number):
    if(number % counter == 0):
      sum += counter
    counter += 1
  
  if (sum == number):
    return True

  return False
