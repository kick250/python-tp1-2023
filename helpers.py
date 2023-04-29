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