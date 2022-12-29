from collections.abc import Iterator


class MyIterator(Iterator):
  def __init__(self, start, end):
    self.start = start
    self.end = end
    
  def __getitem__(self, index):
    if index < 0 or index >= self.end - self.start:
      raise IndexError('Index out of range')
    
    return self.start + index
  
  def __len__(self):
    return self.end - self.start
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.start >= self.end:
      raise StopIteration()
    
    value = self.start
    self.start += 1
    
    return value

iterator = MyIterator(5, 10)

for i in iterator:
  print(i)