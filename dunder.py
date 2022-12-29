class Teste:
  def __new__(cls, *args, **kwargs):
    print('Creating...', args, kwargs)
    
    return super().__new__(cls)
  
  def __init__(self, nome):
    self.nome = nome
    self._is_open = False

  def __str__(self):
    return f'Teste: {self.nome!r}'

  def __repr__(self):
    return f'Teste({self.nome!r})'

  def open(self):
    print('Opening...')
    self._is_open = True
    
  def close(self):
    print('Closing...')
    self._is_open = False
    
  def __enter__(self):
    self.open()
    return self
  
  def __exit__(self, exc_type, exc_value, traceback):
    print('Exiting...', exc_type, exc_value, traceback)
    
    self.close()
    
  def __del__(self):
    print('Deleting...', self.nome)
  
  def __add__(self, other):
    print('Dividing...')
    return Teste(f'{self.nome} {other.nome}')
  
  def __call__(self):
    print('Calling...')
    return self.nome

teste = Teste('Meu teste')
teste2 = Teste('Outro teste')

# print(f'{teste!s}')
# print(f'{teste!r}')

with teste as t:
  print('Teste:', t.nome)


teste3 = teste + teste2

print(f'{teste3!r}')