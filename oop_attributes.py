class Cat():

  #class object attribute
  #this is true for EVERY instance of Cat
  species = "mammal"

  #each cat will have these attributes
  #they will be unique for each instance of Cat
  def __init__(self,breed,name):
    self.breed = breed #attribute 1
    self.name = name #attribute 2

mycat = Cat(breed = "MaineCoon",name = "Mittens")
print(mycat.breed) # => MaineCoon
print(mycat.name) # => Mittens
yourcat = Cat("Persian","Socks")
print(yourcat.breed) # => Persian
print(yourcat.name) # => Socks
print(mycat.species) # => mammal
print(yourcat.species) # => mammal