def my_factorial(n):
  if n == 0:
    return 1
  else:
    return n * my_factorial(n-1)