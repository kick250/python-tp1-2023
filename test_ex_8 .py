import ex_8


def test_get_first_position_of_existing_value():
  existing_value = 5
  vector = (1, 1, existing_value, 1, 5)

  assert ex_8.get_first_position_of(vector, existing_value) == 2

def test_get_first_position_of_not_existing_value():
  existing_value = 10
  vector = (1, 1, 5, 1, 5)

  assert ex_8.get_first_position_of(vector, existing_value) == -1
