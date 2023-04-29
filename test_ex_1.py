import ex_1

def test_sum_of_tuple():
  tuples_to_calc = ((1,5,6,10), (2,4,6,8), (2,), (10,20,30,10,80))

  expected_result = (22, 20, 2, 150)

  assert ex_1.sum_each_tuple(tuples_to_calc) == expected_result

def teste_calc_median_of_list():
  values = (22, 20, 2, 150)

  expected_result = 48.5

  assert ex_1.medium(values) == expected_result