class InvalidVectorException(Exception):
  @property
  def message(self):
    return "Vetor inválido digitado."

class InvalidVectorLengthException(Exception):
  @property
  def message(self):
    return "Tamanho do vetor inválido."

class InvalidValueRangeException(Exception):
  def __init__(self, start_range, end_range):
    self.start_range = start_range
    self.end_range = end_range
    super()

  @property
  def message(self):
    return f"Os valores dos vetor devem estar em um intervalo de {self.start_range}-{self.end_range}."
