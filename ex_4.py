from unidecode import unidecode


def is_from_terminal():
  return __name__ == '__main__'

def is_palindrome(sentence):
    value = str(sentence).lower().replace(" ", "")
    value = unidecode(value)
    return value == value[::-1]

def main():
    sentence = input("Diga a palavra: ").strip()
    if is_palindrome(sentence):
        print("Essa palavra é um palindromo")
    else:
        print("Essa palavar não é um palindromo")


if is_from_terminal():
   main()