import ex_10


def test_vector_length():
  assert ex_10.VECTOR_LENGTH == 20

def test_is_positive():
  positive_value = 10
  not_positive_value = -10

  assert ex_10.is_positive(positive_value)
  assert not ex_10.is_positive(not_positive_value)

def test_get_positive_values():
  vector = (-1, -10, 10, 1, 20, 10)

  result = ex_10.get_positive_values_from(vector)
  assert result == (10, 1, 20, 10)

def test_get_unique_values():
  vector = (10, 10, 13, -10, 11, 12, 10, -1)

  result = ex_10.get_unique_velues_from(vector)

  for value in vector:
    assert result.count(value) == 1