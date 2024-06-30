class Countdown:
  """
  An iterator class that counts down from a given number to 1.

  Raises:
      ValueError: If the start_value is less than 1.
  """
  def __init__(self, start_value):
    if start_value < 1:
      raise ValueError("Start value must be greater than or equal to 1")
    self.start_value = start_value

  def __iter__(self):
    return self

  def __next__(self):
    if self.start_value > 0:
      value = self.start_value
      self.start_value -= 1
      return value
    else:
      raise StopIteration

def fibonacci_generator(limit):
  """
  A generator function that yields Fibonacci numbers up to a specified limit.
  The Fibonacci sequence is a famous series of numbers where each number is the sum of the two preceding ones.
  It starts with 0 and 1.

  Args:
      limit (int): The maximum Fibonacci number to yield.

  Raises:
      ValueError: If the limit is less than or equal to 0.
  """
  if limit <= 0:
    raise ValueError("Limit must be greater than 0")
  a, b = 0, 1
  while a < limit:
    yield a
    a, b = b, a + b

def random_number_generator(min_value, max_value):
  """
  A generator function that yields a sequence of random numbers between a specified range.

  Args:
      min_value (float): The minimum value (inclusive) for the random numbers.
      max_value (float): The maximum value (inclusive) for the random numbers.
  """
  import random
  while True:
    yield random.uniform(min_value, max_value)  # Uniform distribution for continuous range

# Demonstration

# Countdown (starting from 10)
print("Countdown:")
for num in Countdown(10):
  print(num)

# Fibonacci sequence (up to 15)
print("\nFibonacci sequence (up to 15):")
for num in fibonacci_generator(15):
  print(num)

# Random numbers (between 5 and 20, 3 numbers)
print("\nRandom numbers (between 5 and 20):")
for _ in range(3):
  print(next(random_number_generator(5, 20)))
