from enum import Enum, auto

class Direcoes(Enum):
  DIREITA = auto()
  ESQUERDA = auto()
  CIMA = auto()
  BAIXO = auto()

print(Direcoes.ESQUERDA.name, Direcoes.ESQUERDA.value)
