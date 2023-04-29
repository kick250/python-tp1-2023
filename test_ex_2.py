import ex_2

def test_generate_series():
    length_of_serie = 3
    serie = ex_2.generate_serie(length_of_serie)

    assert length_of_serie == len(serie)
    assert serie == ((1, 1), (2, 3), (3, 5))

def test_sum_of_series():
    serie = ((1, 1), (2, 3), (3, 5))

    expected_result = 2.2666666666666666

    assert expected_result == ex_2.sum_serie(serie)