class Person:
  def __init__(self, first_name, last_name, age):
    self.first_name = first_name
    self.last_name = last_name
    self._age = age
  
  @classmethod
  def createPerson(cls, *args):
    return cls(*args)
  
  @staticmethod
  def logger(log):
    print(log)
    
  @property
  def age(self):
    return self._age

  @age.setter
  def age(self, age):
    self._age = age
  
john = Person('John', 'Harris')

mary = john.createPerson('Mary', 'Curie')

print(vars(john))
print(vars(mary))

john.logger('Static method')


mary.full_name = 'Complete name';

mary._age = 20

print(mary.full_name)