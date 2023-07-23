# Python Data Type - Sets  (Unique Values)

# Sample Set
# First define a Set
my_data = {1,2,3,4,1,2,3,4}

# Then call using set() function
my_set = set(my_data)
print(my_set)

# Append an existing Set  (Only one value at a time)
my_set.add(5)
print(my_set)

# Update an existing Set using another Set
my_data2 = {6,7,8,9,10}
my_set.update(my_data2)
print(my_set)