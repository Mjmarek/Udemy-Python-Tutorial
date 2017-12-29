#Lists are Python's form of arrays
my_list = [1,2,3]

#prints length of list
print(len(my_list))
#can have multiple types in lists
my_list2 = ['string',1,1.5,True,[3,4,5]]
print(my_list2)
#index into list => 1.5
print(my_list2[2])
#prints last item in list => [3,4,5]
print(my_list2[-1])
#slicing, prints list up to index 3 => ['string',1,1.5]
print(my_list2[:3])

#lists (unlike strings) are mutable
my_list[0] = 4
print(my_list) # => [4,2,3]
#append adds one item to END of list
my_list.append(5)
print(my_list) # => [4, 2, 3, 5]
#extend used to add multiple items to end of list
more_numbers = [6,7,8]
my_list.extend(more_numbers)
print(my_list) # => [4, 2, 3, 5, 6, 7, 8]
#removes last item from list
item = my_list.pop()
print(my_list) # => [4, 2, 3, 5, 6, 7]
print(item) # => 8
#can specify index for pop
item = my_list.pop(0)
print(my_list) # => [2, 3, 5, 6, 7]
print(item) # => 4
#reverse list & reassigns to that variable
my_list.reverse()
print(my_list) # => [7, 6, 5, 3, 2]

#sort ascending alphabetically or numerically
my_list_let = ['r','y','h','d','c','n']
my_list_let.sort()
print(my_list_let) # => ['c', 'd', 'h', 'n', 'r', 'y']
my_list_num = [5,7,2,9,8,3]
my_list_num.sort()
print(my_list_num) # => [2, 3, 5, 7, 8, 9]

#index into nested lists
my_nested_list = [1,2,['x','y','z']]
print(my_nested_list[2][1]) # => y

#list comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][0]) # => 1
#row represents each item in list
first_col = [row[0] for row in matrix]
print(first_col) # => [1,4,7]


