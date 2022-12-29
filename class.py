from abc import ABC, abstractmethod

class Person(ABC):
  def __init__(self, first_name, last_name, age):
    self.first_name = first_name
    self.last_name = last_name
    # Protected
    self._age = age
    # Private
    self.__salary = 1000
  
  def getFullName(self):
    return f'{self.first_name} {self.last_name}'
  
  @abstractmethod
  def login(self): ...
  
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
  def __init__(self, first_name, last_name, age, email, password):
    super().__init__(first_name, last_name, age)
    self.email = email
    self.password = password
  
  def getFullName(self):
    return f'User: {self.first_name} {self.last_name},'
  
  def login(self):
    print(f'{self.getFullName()} logged in')

class Admin(User):
  def getFullName(self):
    return super(User, self).getFullName()

# help(Admin)

Admin('John', 'Harris', 30, 'john@gmail.com', '12345678').login()

print(Admin.mro())