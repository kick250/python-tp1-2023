from exceptions import InvalidVectorException, InvalidVectorLengthException, InvalidValueRangeException


VECTOR_LENGTH = 2

def verify_range(start_range, end_range, value):
  if start_range != None and start_range > value:
    raise InvalidValueRangeException(start_range, end_range)
  if end_range != None and end_range < value:
    raise InvalidValueRangeException(start_range, end_range)

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

def convert_vector_from_text(vector_text,
    separator = ',',
    vector_length = None,
    start_range = None,
    end_range = None
    ):
  vector = []

  for value in vector_text.split(separator):
    try:
      converted_value = int(value.strip())
      verify_range(start_range, end_range, converted_value)
    except ValueError:
      raise InvalidVectorException()
    vector.append(converted_value)

  if vector_length != None and len(vector) != vector_length:
    raise InvalidVectorLengthException()

  return tuple(vector)

def read_vector_with_text(
    message = "Digite o vetor sepado por virgula:\n",
    separator = ',',
    vector_length = None,
    start_range = None,
    end_range = None
    ):
  vector = None
  while vector == None:
    text = input(message)
    try:
      vector = convert_vector_from_text(text, separator=separator, vector_length=vector_length, start_range=start_range, end_range=end_range)
    except (
        InvalidVectorException,
        InvalidVectorLengthException, InvalidValueRangeException
      ) as ex:
      print(ex.message)
  return vector