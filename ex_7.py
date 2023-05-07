from helpers import ask_number, read_vector


VECTOR_LENGTH = 10

def count_unique_values(vector):
  return len(set(vector))

def main():
  vector = read_vector(vector_length=VECTOR_LENGTH)

  unique_values_quantity = count_unique_values(vector)

  print(f"Vetor => {vector}")
  print(f"Esse vetor possui {unique_values_quantity} {'valor diferente' if unique_values_quantity == 1 else 'valores diferentes'}.")

if  __name__ == '__main__':
  main()