def power(base, exponent):
  """
  Calculates the power of a number.

  Args:
      base (int or float): The base number.
      exponent (int): The exponent.

  Returns:
      int or float: The result of base raised to the power of exponent.
  """
  return base ** exponent

def sqrt(number):
  """
  Calculates the square root of a number.

  Args:
      number (int or float): The number whose square root is to be calculated.

  Returns:
      float: The square root of the number.
  """
  import math  # Import the built-in math module for sqrt
  return math.sqrt(number)
