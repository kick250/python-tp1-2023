import ex_3

def test_generate_sum_of_values():
    values = [1, 2, 3, 4, 5, 6]
    values_sums = ex_3.cumsum(values)

    assert values_sums == [1, 3, 6, 10, 15, 21]


