from random import randint
from datetime import datetime

CLASS_LENGTH = 23
SAMPLE_LENGTH = 2000
START_2002_TIMESTAMP = 1009854000.0
END_2002_TIMESTAMP = 1041389999.0

def is_from_terminal():
  return __name__ == '__main__'

def generate_random_birthdate():
  random_timestamp = randint(START_2002_TIMESTAMP, END_2002_TIMESTAMP)
  return datetime.fromtimestamp(random_timestamp).date()

def calc_probability():
  cases = 0

  for class_i in range(SAMPLE_LENGTH):
    students_birthdates = []
    for student_i in range(CLASS_LENGTH):
      birthdate = str(generate_random_birthdate())
      if students_birthdates.count(birthdate) > 0:
        cases += 1
        break
      students_birthdates.append(birthdate)

  return cases / SAMPLE_LENGTH

def main():
  probability = f"{calc_probability() * 100}%"
  print(f"A probabilidade de 2 alunos fazerem aniversário no mesmo dia é de {probability}")

if is_from_terminal():
  main()