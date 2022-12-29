class Meta(type):
  def __new__(mcs, name, bases, dct):
    print(f'- {mcs}', name, bases, dct, sep='\n- ')

    cls = super().__new__(mcs, name, bases, dct)

    print('cls:', cls)

    return cls

  def __call__(cls, *args):
    print('Calling...', args)

    return super().__call__(*args)


class Person(metaclass=Meta):
  def __new__(cls, *args):
    print('Creating...', args)
    
    return super().__new__(cls)
  
  def __init__(self, name):
    self.name = name

  def speak(self):
    print(f'Hello, my name is {self.name}')


p= Person('Pedro')
