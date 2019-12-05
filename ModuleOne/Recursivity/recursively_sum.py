def recursive_sum(n):
  if n < 1:
    return 0
  elif n == 1:
    return n
  return n + recursive_sum(n - 1)

print(recursive_sum(10))