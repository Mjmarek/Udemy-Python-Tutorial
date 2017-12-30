#Bools
True # also 0
False # also 1

#Tuples
#very similar to lists
#only difference is tuples are immutable
t = (1,2,3)
print(t[0])

#Sets
#unordered collection of unique elements
x = set()
x.add(1)
x.add(2)
x.add(0.5)
x.add(3)
print(x) # => {0.5, 1, 2, 3}
#only takes in 1 unique element
converted = set([1,1,1,1,2,2,2,3,3,3,3,3])
print(converted) # => {1, 2, 3}