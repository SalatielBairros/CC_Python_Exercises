def sum(user_input):
  sum = user_input
  strRet = str(user_input)
  for n in range(user_input - 1):
    sum += user_input
    strRet += " + " + str(user_input)
  
  return strRet + " = " + str(sum)

print(sum(5))
print(sum(0))
