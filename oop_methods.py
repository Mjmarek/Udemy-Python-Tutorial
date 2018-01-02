class Circle():  
  pi = 3.14

  #here, providing default value of 1 for radius
  def __init__(self, radius = 1):
    self.radius = radius

  def area(self):
    return self.radius*self.radius*Circle.pi

  #can create method to change attribute
  def set_radius(self, new_r):
    self.radius = new_r
  
mycircle = Circle(3)
print(mycircle.radius) # => 3
print(mycircle.area()) # => 28.26

#one way to change attributes in class
mycircle.radius = 5
print(mycircle.area()) # => 78.5

#another way to change attributes in class via method
mycircle.set_radius(10)
print(mycircle.area()) # => 314.0