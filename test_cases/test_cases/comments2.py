def factorial(n):
  # Calculate the factorial
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)