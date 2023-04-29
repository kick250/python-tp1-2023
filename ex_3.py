def is_from_terminal():
  return __name__ == '__main__'


def cumsum(values):
    values_sums = []

    values_sum = 0
    for value in values:
        values_sum += value
        values_sums.append(values_sum)

    return values_sums

def main():
    values = [1, 2, 3, 4, 5, 6]
    values_sums = cumsum(values)
    print(values_sums)


if is_from_terminal():
   main()