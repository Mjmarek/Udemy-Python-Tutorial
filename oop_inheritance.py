#derived classes inherit from base classes

#Base Class
class Animal():
  def __init__(self):
    print("Animal Created")
  def whoAmI(self):
    print("Animal")
  def eat(self):
    print("Eating")

#pass in base class to derived class
class Cat(Animal):
  def __init__(self):
    #Animal.__init__(self) - this line not needed
    print("Cat Created")
  def meow(self):
    print("Purr")
  #can override methods from base class
  def eat(self):
    print("Cat Eating")

mycat = Cat() # => Cate Created
mycat.whoAmI() # => Animal
mycat.eat() # => Cat Eating
mycat.meow() # => Purr