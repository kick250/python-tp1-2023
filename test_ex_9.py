import ex_9


def test_roll_dice():
  results = [ex_9.roll_dice() for i in range(100)]
  assert results.count(1) > 0
  assert results.count(2) > 0
  assert results.count(3) > 0
  assert results.count(4) > 0
  assert results.count(5) > 0
  assert results.count(6) > 0

def test_calc_porcent_to_get_6():
  dice_results = [6, 6, 6, 6, 6, 1, 2, 3, 4, 5]
  assert ex_9.calc_porcent_to_get_6(dice_results, sample_length = 10) == 50.0