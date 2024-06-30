# File paths for reference (not used in this example)
file_path = "data.txt"
output_file = "output.txt"

def read_file(file_path):
  """
  Reads data from a text file and prints its contents.

  Args:
      file_path (str): Path to the text file.

  Returns:
      None: This function only prints the contents and doesn't return a value.
  """
  try:
    with open(file_path, 'r') as file:
      contents = file.read()
      print(contents)
  except FileNotFoundError:
    print(f"Error: The file {file_path} was not found.")
  except PermissionError:  # More specific exception for permission issues
    print(f"Error: Insufficient permissions to access {file_path}.")
  except IOError as e:  # Catching other potential IO errors
    print(f"Error: An error occurred while reading {file_path}: {e}")

print("Reading data.txt...")
read_file(file_path)


def write_to_file(filename, data):
  """
  Writes user input to a new file.

  Args:
      filename (str): Name of the output file.
      data (str): The data to write to the file.
  """
  try:
    with open(filename, 'w') as f:
      f.write(data)
  except IOError as e:
    print(f"Error: An error occurred while writing to {filename}: {e}")

user_input = input('Enter some text to write to a new file: ')
write_to_file(output_file, user_input)


def count_words(filename):
  """
  Counts the number of words in a text file.

  Args:
      filename (str): Path to the text file.

  Returns:
      int: The number of words in the file.
  """
  try:
    with open(filename, 'r') as f:
      contents = f.read()
      word_count = len(contents.split())
      return word_count
  except FileNotFoundError:
    print('Error: File not found.')
  except IOError as e:
    print(f"Error: An error occurred while reading {filename}: {e}")

word_count = count_words(file_path)
print(f'Number of words in data.txt: {word_count}')
 
