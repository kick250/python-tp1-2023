from helpers import read_vector_with_text


START_RANGE = 1
END_RANGE = 13
ASC = "asc"
DESC = "desc"
NOT_SORTED = "not_sorted"
TRANSLATED_SEQUENCE_TYPES = {
  ASC: "C",
  DESC: "D",
  NOT_SORTED: "N"
}

def translate_sequence_type(type):
  return TRANSLATED_SEQUENCE_TYPES[type]

def get_sequence_type(sequence):
  is_asc = True
  is_desc = True

  for index, number in enumerate(sequence):
    if index == 0: continue

    last_number = sequence[index - 1]
    if is_asc and number < last_number:
      is_asc = False
    elif is_desc and number > last_number:
      is_desc = False

  if is_asc: return ASC
  if is_desc: return DESC
  return NOT_SORTED

def main():
  sequence = read_vector_with_text(
    message="Digite a 5 números separados por espaço: ",
    separator=" ",
    vector_length=5,
    start_range=START_RANGE,
    end_range=END_RANGE
  )
  print(sequence)
  sequence_type = get_sequence_type(sequence)
  print(translate_sequence_type(sequence_type))


if  __name__ == '__main__':
  main()