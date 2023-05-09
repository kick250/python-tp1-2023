from helpers import ask_number, read_vector_with_text


def main():
  vector = read_vector_with_text()
  number = ask_number(message="Digite o número que você quer contar: ")
  quantity = vector.count(number)

  print(f"Vetor => {vector}")
  print(f"O número {number} apareceu {quantity} {'vez' if (quantity == 1) else 'vezes'} no vetor.")


if  __name__ == '__main__':
  main()