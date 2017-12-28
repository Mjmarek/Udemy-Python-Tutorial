mystring = 'abcdefg'

#Indexing
#prints the last index => g
print(mystring[-1]) 

#Slicing
#grabs 3rd index to the end => defg
print(mystring[3:])
#grabs everything up to but NOT including 4th index => abcd
print(mystring[:4])
#grabs 2nd, 3rd, and 4th index (not 5th) => cde
print(mystring[2:5])
#both of these print the whole string
print(mystring[:])
print(mystring[::])
#can define step size(2) => aceg
print(mystring[::2])

#Split
mystring = "Hello World"
#splits on whitespace by default
x = mystring.split()
print(x) # => ['Hello', 'World']
#can also choose what to split on
x = mystring.split('r')
print(x) # => ['Hello Wo', 'ld']
x = mystring.split('o')
print(x) # =>['Hell', ' W', 'rld']

#String Interpolation
x = "Insert another string here: {}".format("INSERT ME!")
print(x) # => Insert another string here: INSERT ME!
x = "Item 1: {y}, Item 2: {z}".format(y="apples",z="oranges")
print(x) # => Item 1: apples, Item 2: oranges