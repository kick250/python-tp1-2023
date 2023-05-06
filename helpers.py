VECTOR_LENGTH = 2

def ask_number(message = "Digite um numero: "):
  value_parsed = None
  while value_parsed == None:
    try:
      value = input(message).strip()
      value_parsed = int(value)
    except ValueError:
      print("valor invalido digitado.")
      next
  return value_parsed

def read_vector(vector_length = VECTOR_LENGTH):
  vector = []
  for i in range(vector_length):
    print(f"Vetor atual: {vector}")
    value = ask_number(message=f"Qual o valor da posição {i}? ")
    vector.append(value)
  return tuple(vector)