from typing import TypeVar

T = TypeVar('T')


def getItem(items: list[T], index: int) -> T:
  return items[index]


print(getItem([1, 2, 3], 0))


def teste(a, b, /, *, c, d):
  print(a, b, c, d)

teste(1, 2, c=3, d=4);