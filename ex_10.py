from helpers import read_vector


VECTOR_LENGTH = 20

def is_positive(value):
  return value > 0

def get_positive_values_from(vector):
  return tuple(filter(is_positive, vector))

def get_unique_velues_from(vector):
  return tuple(set(vector))

def main():
  vector = read_vector(vector_length=VECTOR_LENGTH)
  positive_values_vector = get_positive_values_from(vector)
  unique_values_vector = get_unique_velues_from(positive_values_vector)

  print(f"Vetor completo => {vector}")
  print(f"Vetor de valores positivos => {positive_values_vector}")
  print(f"Vetor de valores únicos => {unique_values_vector}")


if  __name__ == '__main__':
  main()