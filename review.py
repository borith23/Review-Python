class myNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x 
myClass = myNumber()
myIter = iter(myClass)

print(next(myIter))
print(next(myIter))



def myfunc():
  k = 300
  def myinnerfunc():
    print(k)
  myinnerfunc()

myfunc()

# import platform

# x = dir(platform)
# print(x)

print("----------------")

i = "apple"
for k in i:
    print(k)
    break
    
print("hello")

print("----------------")

class MyNumbers:
  def __iter__(self):
    self.a = 15
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
