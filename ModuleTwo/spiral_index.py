def spiral_index(x, y):
  mX = abs(x)
  mY = abs(y)
  ret = 0

  if(mX == mY and x != y):
    odd = 1 if (x > 0 and y < 0) else 0
    ret = pow((2 * x) + odd, 2) - odd
  elif((mX - mY == 1) and x > 0 and y < 0):
    ret = pow((2 * (x - 1)) + 1, 2)
  else:
    mM = mX if mX > mY else mY
    iM = mM * -1

    if(x > iM and y >= 0):
      if(y > x):
        ret = pow_num(mM -1) + total_distance(x, y, mM, iM)
      else:
        ret = pow_num(mM -1) + total_distance(x, y, (mM - 1), (iM + 1))
    else:
      ret = pow_num(mM) - total_distance(x, y, mM, iM)

  print('Spiral index of (' + str(x) + ', ' + str(y) + ') is ' + str(ret) + '.')
  pass

def total_distance(x1, y1, x2, y2):
  return (abs(x2 - x1) + abs(y2 - y1))

def pow_num(x):
  return pow((2 * x) + 1, 2) - 1

spiral_index(2, -1)  
spiral_index(-3, 3)  
spiral_index(10, 10)  
spiral_index(10, -10)  
spiral_index(5, -10)  
spiral_index(3, 15)  
spiral_index(1000, 1000)  