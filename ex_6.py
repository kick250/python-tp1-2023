from helpers import ask_number

VECTORS_QUANTITY = 2
VECTOR_LENGTH = 3

def is_from_terminal():
  return __name__ == '__main__'

def read_vector():
  vector = []
  for i in range(VECTOR_LENGTH):
    print(f"Vetor atual: {vector}")
    value = ask_number(message=f"Qual o valor da posição {i}? ")
    vector.append(value)
  return tuple(vector)

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
    vectors.append(read_vector())

  result = sum_vectors(vectors)
  for index, vector in enumerate(vectors):
    print(f"Vetor {index + 1} => {vector}")

  print(f"resultado da soma: {result}")

if is_from_terminal():
  main()