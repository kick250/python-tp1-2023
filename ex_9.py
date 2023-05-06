from random import randint


SAMPLE_LENGTH = 50
DICE_START = 1
DICE_END = 6

def roll_dice():
  return randint(DICE_START, DICE_END)

def calc_porcent_to_get_6(dice_results, sample_length = SAMPLE_LENGTH):
  cases = dice_results.count(6)
  porcent = cases / sample_length
  return porcent * 100

def main():
  dice_results = []
  for i in range(SAMPLE_LENGTH):
    dice_results.append(roll_dice())
  porcent = calc_porcent_to_get_6(dice_results)
  print(f"O número 6 teve {porcent}% de aparecimento.")


if  __name__ == '__main__':
  main()