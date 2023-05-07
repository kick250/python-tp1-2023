import ex_11
from exceptions import InvalidVectorException

def test_convert_vector_from_text():
  vector_text = "1, 67, 78, 34, 90, 876, 0, 12, 8, 3, 56, 987, 3, 2,45,12,10, 45"

  vector = ex_11.convert_vector_from_text(vector_text)
  expected_vector = (1, 67, 78, 34, 90, 876, 0, 12, 8, 3, 56, 987, 3, 2, 45, 12, 10, 45)
  assert vector == expected_vector

def test_convert_vector_from_text_when_invalid():
  vector_text = "1, Batata, 78"

  try:
    ex_11.convert_vector_from_text(vector_text)
    assert False
  except InvalidVectorException as exception:
    assert True
    assert exception.message == "Vetor inválido digitado."
  except:
    assert False