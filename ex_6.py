from helpers import read_vector


VECTORS_QUANTITY = 2
VECTOR_LENGTH = 3

def sum_vectors(vectors_list):
  result = [0 for i in range(VECTOR_LENGTH)]

  for vector in vectors_list:
    for value_index, value in enumerate(vector):
      result[value_index] += value

  return tuple(result)

def main():
  vectors = []
  for i in (1, VECTORS_QUANTITY):
    print(f"Diga os valores do vetor {i}")
    vector = read_vector(vector_length = VECTOR_LENGTH)
    vectors.append(vector)

  result = sum_vectors(vectors)
  for index, vector in enumerate(vectors):
    print(f"Vetor {index + 1} => {vector}")

  print(f"resultado da soma: {result}")

if  __name__ == '__main__':
  main()