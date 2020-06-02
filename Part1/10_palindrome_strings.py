def palindrome(input_str):
  return input_str[::-1] == input_str


def max_sub_palindrome(input_str):
  for n in range(len(input_str), -1, -1):
    sub = sub_palindrome(input_str, n)
    if(sub is not None):
      return sub
  pass

def sub_palindrome(input_str, size):
  sizeDiff = (len(input_str) - size) + 1
  if(sizeDiff > 0):
    for i in range(sizeDiff):
      print(input_str[i:(i + size)])
      if(palindrome(input_str[i:(i + size)])):
        return input_str[i:(i + size)]
  elif(palindrome(input_str)):
    return input_str
  return None

print(max_sub_palindrome("ccAABBAd"))