import ex_5

def test_generate_random_birthdate():
  birthdate_1 = ex_5.generate_random_birthdate()

  assert str(type(birthdate_1)) == "<class 'datetime.date'>"

def test_calculate_probability():
  probability = ex_5.calc_probability()

  assert probability > 0.4 and probability < 0.6