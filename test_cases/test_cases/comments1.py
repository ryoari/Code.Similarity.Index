def factorial(n):
  # This function calculates the factorial of a number
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)