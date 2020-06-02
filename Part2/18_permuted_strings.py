def is_permutation(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    if(len1 == 0 or len2 == 0 or len1 != len2):
      if(len1 == 0 and len2 == 0):
        return True
      return False
    
    ls1 = sorted(str1)
    ls2 = sorted(str2)

    for i in range(len1):
      if(ls1[i] != ls2[i]):
        return False

    return True


def get_permutation_list(input_str, output_str):
    permutationIndex = []
    
    for co in output_str:
      for i in range(len(input_str)):
        if(co == input_str[i] and i not in permutationIndex):
          permutationIndex.append(i)
          break

    return permutationIndex

print(is_permutation("salatiel", "leitalas"))
print(is_permutation("", ""))
print(get_permutation_list("salatiel", "leitalas"))