def sorted_matrix_search(matrix, integer):
  rowsNumber = len(matrix)
  if(rowsNumber == 0):
    return None
  
  columnsNumber = len(matrix[0])

  for i in range(columnsNumber):
    value = matrix[i][columnsNumber - 1]
    if(value >= integer):
      for j in range(rowsNumber):
        value = matrix[i][j]
        if(value == integer):
          return (i, j)

  return None

m = [
  [0, 58],
  [62, 72]
]

print(sorted_matrix_search(m, 62))