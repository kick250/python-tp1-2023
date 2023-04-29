from helpers import ask_number

def is_from_terminal():
  return __name__ == '__main__'

def generate_serie(length):
    serie = []
    value_N = 1
    value_M = 1

    for i in range(length):
        serie.append((value_N, value_M))
        value_N += 1
        value_M += 2

    return tuple(serie)

def sum_serie(series):
    values = []
    for serie in series:
        values.append(serie[0] / serie[1])
    return sum(values)

def main():
    length = ask_number(message = "Qual o tamanho da series? ")

    serie = generate_serie(length)

    for index, values in enumerate(serie):
        is_last_serie = index == len(serie) - 1
        print(f"{values[0]}/{values[1]}", end = "")
        if is_last_serie:
            print()
            continue
            
        print(" + ", end = "")

    print(f"Resultado => {sum_serie(serie)}")


if is_from_terminal():
  main()