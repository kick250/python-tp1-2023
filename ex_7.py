from helpers import ask_number, read_vector


VECTOR_LENGTH = 10

def count_occurrences(vector, number):
  return vector.count(number)

def main():
  vector = read_vector(vector_length=VECTOR_LENGTH)
  number = ask_number(message="Digite o número que você quer contar: ")

  quantity = count_occurrences(vector, number)

  print(f"Vetor => {vector}")
  print(f"O número {number} aparece {quantity} {'vez' if (quantity == 1) else 'vezes'} no vetor.")


if  __name__ == '__main__':
  main()