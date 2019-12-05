def coprime(a, b):
  while b != 0:
    a, b = b, a % b    
  return a == 1

def count_coprimes(n):
  count = 1
  for i in range(n)[2::]:
    if(coprime(i, n)):
      count += 1
  
  return count

print(count_coprimes(86))
