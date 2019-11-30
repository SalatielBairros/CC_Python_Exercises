def cubic_root(n):
    response = 2
    diference = 0

    if(n >= 0):
        if (n < 2):
          return n

        cube = response * response * response
        while(cube < n):
            response += 1
            cube = response * response * response

        response -= 1
