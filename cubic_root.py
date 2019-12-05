def cubic_root(n):
    response = 2
    diference = 0

    if(n >= 0):
        if (n < 2):
          response = n
        else:
          while((response * response * response) <= n):
              response += 1
          response -= 1

        diff = n - (response * response * response)
        isExact = "exact!" if diff == 0 else "not exact"
        # Interpolation does not work at Python 2.
        # diffMessage = f"with difference {diff}"
        diffMessage = "" if diff == 0 else "with difference " + str(diff)
        message = str(response) + ", " + isExact + " " + diffMessage
        # print(f"{response}, {isExact} {diffMessage}")
        print(message)

    pass

cubic_root(99)