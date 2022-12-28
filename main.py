class Person:
  def __init__(self, first_name, last_name, age):
    self.first_name = first_name
    self.last_name = last_name
    # Protected
    self._age = age
    # Private
    self.__salary = 1000
  
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
    
  @property
  def salary(self):
    return self.__salary
  
  @salary.setter
  def salary(self, salary):
    self.__salary = salary

class User(Person):
  def login(self):
    print(f'User ${self.first_name} ${self.last_name} logged in')
  
john = Person('John', 'Harris', 30)

mary = john.createPerson('Mary', 'Curie', 25)

print(vars(john))
print(vars(mary))

help(Person)