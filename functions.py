def my_func(param1 ='default'):
  """
  Hover over my_func to see this text
  """
  print("my first python function")
my_func() # => my first python function

def hello():
  return "hello"
result = hello()
print(result) # => hello

#Filter function
mylist = [1,2,3,4,5,6,7,8]
def even_bool(num):
  return num%2 == 0
evens = filter(even_bool,mylist)
print(list(evens)) # => [2, 4, 6, 8]

#Lambda expression/Anonymous function
#same as above using lambda instead
mylist = [1,2,3,4,5,6,7,8]
evens = filter(lambda num:num%2 == 0, mylist)
print(list(evens)) # => [2, 4, 6, 8]
