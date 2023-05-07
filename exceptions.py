class InvalidVectorException(Exception):
  @property
  def message(self):
    return "Vetor inválido digitado."