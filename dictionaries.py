#Dictionaries are Python's version of hash tables
#Also similar to objects in JavaScript

my_stuff = {"key1":"value","key2":"value2"}
print(my_stuff["key2"]) # => value2

#can mix types
my_stuff1 = {'key1':234,'key2':'value2','key3':{'123':[1,2,3]}}
#order not necessarily retained when printed (here it is)
print(my_stuff1) # => {'key1': 234, 'key2': 'value2', 'key3': {'123': [1, 2, 3]}}
#print specific values within nested dictionaries
my_stuff2 = {'key1':234,'key2':'value2','key3':{'123':[1,2,'print_me']}}
print(my_stuff2['key3']['123'][2]) # => print_me
#can call methods on values
print(my_stuff2['key3']['123'][2].upper()) # => PRINT_ME

#can redefine dictionary items
meals = {'lunch':'pizza','dinner':'pasta'}
print(meals['lunch']) # => pizza
meals['lunch'] = 'sandwich'
print(meals['lunch']) # => sandwich
#add items to dictionary
meals['breakfast'] = 'cereal'
print(meals) # => {'lunch': 'sandwich', 'dinner': 'pasta', 'breakfast': 'cereal'}