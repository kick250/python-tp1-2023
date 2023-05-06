from helpers import read_vector, ask_number


VECTOR_LENGTH = 5

def get_first_position_of(vector, number):
  try:
    return vector.index(number)
  except ValueError:
    return -1

def main():
  vector = read_vector(vector_length=VECTOR_LENGTH)
  number = ask_number(message="Digite o número que você quer pegar a posição: ")

  position = get_first_position_of(vector, number)
  print(f"Vetor => {vector}")
  print(f"Posição => {position}")


if  __name__ == '__main__':
  main()