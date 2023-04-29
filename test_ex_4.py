import ex_4


def test_reverse_word():
  sentence = "radar"
  assert ex_4.is_palindrome(sentence) == True

def test_upper_case():
  sentence = "Radar"
  assert ex_4.is_palindrome(sentence) == True

def test_remove_spaces():
  sentence = "Roma me tem amor"
  assert ex_4.is_palindrome(sentence) == True

def test_replace_to_spacial_chars():
  sentence = "Socorram me subi no ônibus em marrocos"
  assert ex_4.is_palindrome(sentence) == True

def test_when_is_not_palindrome():
  sentence = "batata"
  assert ex_4.is_palindrome(sentence) == False