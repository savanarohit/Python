# Print Function - print()

# How to use print() for debugging
my_string1 = 'Hello'
my_string2 = 'World'

# Simple print
print(my_string1 , my_string2)

# Print multiple variables
print("My string is" , my_string1,my_string2)


# Format function - format() is used to format strings by replacing placeholders with corresponding values. It allows you to construct dynamic strings with variables, expressions, and formatted values. This was used in Python Version 2 but from Version 3.6 we use f-strings

# Print using Format
name = "Alice"
age = 25

print("My name is {} and I am {} years old.".format(name, age))

# Positional arguments
item = "Apple"
price = 0.5
quantity = 10

print("Item: {}, Price: ${:.2f}, Quantity: {}".format(item, price, quantity))


# Keyword arguments
name = "Bob"
age = 30

print("Name: {n}, Age: {a}".format(n=name, a=age))


# f-strings
# you can use f-strings (formatted string literals) as a more concise and readable alternative for string formatting. It allows you to directly embed expressions and variables within curly braces

name ='Rohit'
age = 35
print(f"My name is {name} and I am {age} years old.")
