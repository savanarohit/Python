# List Comprehension - List comprehension is a concise way to create lists in Python. It allows you to generate a new list by iterating over an existing sequence (such as a list, tuple, or string), applying a condition or transformation to each element, and optionally filtering the elements based on a given condition.

# Fill blank list using a string

# Normal Method (Without using List Comprehension)
my_string = "hello"
my_list = []

for i in my_string:
    my_list.append(i)
    print(i)
    
print(my_list)

# List Comprehension method
my_string = "hello"
print(my_string)
my_list = [i for i in my_string]
print(my_list)

# List Comprehension with transformation 
my_string = "hello"
print(my_string)
my_list = [i*2 for i in my_string]
print(my_list)

# List Comprehension with Condition
my_list = [i**2 for i in range(0,10) if i % 2 ==0 ]
print(my_list)


# List Comprehension Example - Suppose you have a list of numbers, and you want to filter out the prime numbers from that list using list comprehension. Here's how you can do it:

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# List comprehension to filter prime numbers
prime_numbers = [num for num in numbers if all(num % i != 0 for i in range(2, int(num**0.5) + 1)) and num > 1]

print(prime_numbers)



