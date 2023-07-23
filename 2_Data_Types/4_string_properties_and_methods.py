# String Properties

# Immutability - String Object does not support item assignment
my_name = 'Rohit'
# name = my_name[0] = 'M'
print(my_name)

# String Methods

# Count  - How many time a character is present in a String
my_name = 'Savana'
string_count = my_name.count('a')
print(string_count)

# Count - Same but start from 3rd Index)
my_name = 'Savana'
string_count = my_name.count('a',3)
print(string_count)

# Count - Same but start from 0th and end at 6th Index)
my_name = 'Savana'
string_count = my_name.count('a', 0 , 6)
print(string_count)

# Uppercase
my_name = 'Savana'
string_uppercase = my_name.upper()
print(string_uppercase)

# Lowercase
my_name = 'ROHIT'
string_lower = my_name.lower()
print(string_lower)

# Split method in Python is used to split a string into a list of substrings based on a specified delimiter. It takes one optional argument, the delimiter, which is used to determine where the string should be split.

# Splitting at whitespace
string_sentence = "Hello, how are you?"
words = string_sentence.split()  
print(words)


# Splitting at a Character
my_name = 'savana'
string_split = my_name.split('a')
print(string_split)


# Splitting at Commas
numbers = "1,2,3,4,5"
number_list = numbers.split(",")
print(number_list)

# Real World Example

# User input: Full name separated by a space
full_name = input("Enter your full name: ")

# Splitting the full name into first name and last name
name_parts = full_name.split()

# Accessing the first and last name from the split result
first_name = name_parts[0]
last_name = name_parts[-1]

# Printing the first and last name separately
print("First Name:", first_name)
print("Last Name:", last_name)














