def reverse_digits(n):
  if(n < 10):
    return n
  else:
    sn = str(n)
    last = sn[-1]    
    return int(last + str(reverse_digits(int(sn[:-1]))))

print(reverse_digits(546543132158458232123))