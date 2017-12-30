#Whitespace & indentation important in Python

if 1 < 2:
  print('yes')
  if 20 < 3:
    print('true')

if 1 > 2:
  print('hello')
else:
  print('good bye')

if 1 > 2:
  print('hello')
elif 3 == 3:
  print('equal')
else:
  print('good bye')

#For Loops

#Iterate through list
seq = [1,2,3,4,5,6]
for item in seq:
  print(item)

#Iterate through dictionary (not in order)
d = {"Jill":1,"Jane":2,"Mary":3}
for item in d:
  print(item) #prints values

d = {"Jill":1,"Jane":2,"Mary":3}
for k in d:
  print(k)
  print(d[k]) #prints keys & values

#Iterate through tuple
my_pairs = [(1,2),(3,4),(5,6)]
for item in my_pairs:
  print(item) #prints each pair => (1,2) (3,4) (5,6)

#Unpack tuple
for tup1,tup2 in my_pairs:
  print(tup2)
  print(tup1)
  # => 2 1 4 3 6 5
for tup1,tup2 in my_pairs:
  print(tup1) # => 1 3 5

#While loop
i = 1
while i < 5:
  print("i is: {}".format(i))
  i += 1
# => i is: 1
# => i is: 2
# => i is: 3
# => i is: 4

#Range
new_range = list(range(0,20,2))
print(new_range) # => [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
for item in range(10):
  print(item) # => 0 1 2 3 4 5 6 7 8 9

#List comprehension
x = [1,2,3,4]
#as a for loop
out = []
for num in x:
  out.append(num**2)
print(out) # => [1, 4, 9, 16]
#rewritten in flattened form using comprehension
out = [num**2 for num in x]
print(out) # => [1, 4, 9, 16]