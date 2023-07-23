# Python Functions

# How to get a method information
# 1. Using help() function
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)
print(help(my_list.append))
print(help(my_list.pop))

# 2. Using Python Documentation https://docs.python.org/3/


# Sample Function
def mydemo():
    "Demo Function that print Hello World!"
    print("Hello World!")


mydemo()
print(help(mydemo))


# Function using Arguments
def myargrs(Arguments):
    "Demo Function that print Hello World!"
    print(f"This is {Arguments} Env")


myargrs("Testing")
myargrs("Development")
myargrs("Producion")


# Function arguments with initial values
def sum_of_num(a=10, b=20, c=30):
    return sum([a, b, c])


output = sum_of_num()
print(output)


# Function arguments with no values (If there is any arg with value it should be at last)
def sum_num(b, c, a=10):
    return sum([a, b, c])


output = sum_num(10, 20)  # This is for b and c as a has value of 10
print(output)


# Function with any number of arguments passing using *args
def num_sum(*args):
    print(args)
    return sum(args)


output = num_sum(10, 20, 30, 40)
print(output)


# Function with key-based arguments passing using **kwargs  (It uses Dictionary)
def numsum(**kwargs):
    print(kwargs)


output = numsum(a="10", b="20", c="30")
print(output)


# Function with *args and **kwargs
def sumak(*args, **kwargs):
    print(f"I would like to have: {args[0]} {kwargs['vegetable']}")
    # We can change vegetable to fruit


output = sumak(10, fruit="Mango", vegetable="pupmkin")
print(output)


# Real world Example of *args and **kwargs
def create_invoice(customer_name, *items, **prices):
    "This function create invoice with Customer name,items and price details passed using arguments"
    print("Invoice for:", customer_name)
    print("Items")
    for item in items:
        print("-", item)
    print("Prices")
    for item, price in prices.items():
        print("-", item, ":", price)


# Example usage
create_invoice("Savana Rohit", "Apple", "Mango", Apple=10, Mango=20)
print(help(create_invoice))

# Map function      (To get multiplication of numbers of a List)
my_list = [1, 2, 3, 4, 5]


def square(number):
    return number * 2


output = list(map(square, my_list))
print(output)

# Lambda Function (Inline function)
output = list(map(lambda number: number * 2, my_list))
print(output)

# Filter Function (Inline Filter function)
output = list(filter(lambda x: x % 2 == 0, my_list))
print(output)

# Real World Example of Map function
temperatures_celsius = [25, 30, 35, 40, 15]


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Convert temperatures from Celsius to Fahrenheit using map()
temperatures_fahrenheit = list(map(celsius_to_fahrenheit, temperatures_celsius))
output = list(map(lambda celsius: celsius * 9 / 5 + 32, temperatures_celsius))

print("Temperatures in Celsius:", temperatures_celsius)
print("Temperatures in Fahrenheit:", temperatures_fahrenheit)
print("Temperatures in Fahrenheit:", output)


# Nested Function ( Function inside a Function )
def demo():
    def name():
        print("name function called")

    return 1


output = demo()
print(output)

# Function Scope (LEGB - Local , Enclosing , Global and Built-in)


# Local - Local function variable name assigned within a function and not declared global in function
def my_function():
    x = 10  # Local variable 'x'
    print(x)


my_function()


# Enclosing - Enclosing function local: names in the local scope of any and enclosing functions (def or lambda)
def outer_function():
    y = 20  # Enclosing function local variable 'y'

    def inner_function():
        print(y)  # Accessing enclosing function local variable 'y'

    inner_function()


outer_function()

# Global - Named assigned at the top of a function
z = 30  # Global variable 'z'


def my_function():
    print(z)  # Accessing global variable 'z'


my_function()

# Built-in - Named assigned built in by python modules
import math

print(math.pi)  # Accessing built-in name 'pi' from the 'math' module
