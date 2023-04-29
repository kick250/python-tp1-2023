def is_from_terminal():
  return __name__ == '__main__'

def sum_each_tuple(tuples):
  return tuple([sum(values) for values in tuples])

def medium(tuples_of_values):
  amount = sum(tuples_of_values)
  return amount / len(tuples_of_values)

def main():
  tuples_to_calc = ((1,5,6,10), (2,4,6,8), (2,), (10,20,30,10,80))

  calculed_tuples = sum_each_tuple(tuples_to_calc);
  medium_of_tuples = medium(calculed_tuples)

  for index, value in enumerate(calculed_tuples):
    print(f"{index}: {value}")
  print(f"Média total: {medium_of_tuples}")


if is_from_terminal():
  main()