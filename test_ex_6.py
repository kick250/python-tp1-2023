import ex_6

def test_sum_vectors():
  vectors = [(-1, 1, 50), (-1, 1, 25), (0, 2, 25)]

  result = ex_6.sum_vectors(vectors)

  assert result == (-2, 4, 100)