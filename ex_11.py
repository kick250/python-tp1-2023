from helpers import ask_number
from exceptions import InvalidVectorException


VECTOR_MIN_LENGTH = 10


def convert_vector_from_text(vector_text):
  vector = []

  for value in vector_text.split(','):
    try:
      converted_value = int(value.strip())
    except ValueError:
      raise InvalidVectorException()
    vector.append(converted_value)

  return tuple(vector)

def read_vector_with_text():
  vector = None
  while vector == None:
    text = input("Digite o vetor sepado por virgula:\n")
    try:
      vector = convert_vector_from_text(text)
    except InvalidVectorException as ex:
      print(ex.message)
  return vector

def main():
  vector = read_vector_with_text()
  number = ask_number(message="Digite o número que você quer contar: ")
  quantity = vector.count(number)

  print(f"Vetor => {vector}")
  print(f"O número {number} apareceu {quantity} {'vez' if (quantity == 1) else 'vezes'} no vetor.")


if  __name__ == '__main__':
  main()