import ex_12

# receber 5 numeros separado por espaco
#   As cartas devem ter valor diferentes
#   Os valores devem estar entre 1 e 13
# dizer se a sequencia esta:
#   C => ordenada
#   D => decrescentemente
#   N => nenhum das anteriores

def test_get_sequence_type_when_asc():
  sequence = (1, 3, 9, 11, 12)
  sequence_type = ex_12.get_sequence_type(sequence)
  assert sequence_type == ex_12.ASC

def test_get_sequence_type_when_desc():
  sequence = (10, 9, 5, 2, 1)
  sequence_type = ex_12.get_sequence_type(sequence)
  assert sequence_type == ex_12.DESC

def test_get_sequence_type_when_not_sorted():
  sequence = (10, 12, 11, 2, 3)
  sequence_type = ex_12.get_sequence_type(sequence)
  assert sequence_type == ex_12.NOT_SORTED

def test_translate_sequence_type_when_asc():
  type = ex_12.ASC
  translated_type = ex_12.translate_sequence_type(type)
  assert translated_type == "C"

def test_translate_sequence_type_when_desc():
  type = ex_12.DESC
  translated_type = ex_12.translate_sequence_type(type)
  assert translated_type == "D"

def test_translate_sequence_type_when_not_sorted():
  type = ex_12.NOT_SORTED
  translated_type = ex_12.translate_sequence_type(type)
  assert translated_type == "N"
