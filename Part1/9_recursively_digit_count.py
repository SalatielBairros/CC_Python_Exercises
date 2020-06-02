def count_digits(n):
  if(n == 0):
    return n
  if(n < 0):
    n *= -1
  if(n < 10):
    return 1
  return 1 + count_digits(n/10)