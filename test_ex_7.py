import ex_7

def test_count_occurrences():
  number_to_count = 2
  vector = (1, 1, 1, 1, 1, 1, 1, 1, number_to_count, number_to_count, number_to_count)

  result = ex_7.count_occurrences(vector, number_to_count)
  assert result == 3


