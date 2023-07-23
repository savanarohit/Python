# For loop - to iterate though a loop or do some task with that loop

# Sample for loop (iteration)
number = [1,2,3,4,5]
for item in number:
    print(item)


# Sum using for loop
number = [1,2,3,4]
total = 0       # Don't forget to set total to 0
for item in number:
    total = total + item
    print(total)

# Print Square of a number
number = [1,2,3]
for num in number:
    square = num ** 2
    print(square) 

# Check if a number is even or not
number = [1,2,3,4,5]
for num in number:
    if not num % 2:
        print("Even number:",num)
    else:
        print("Odd number:",num)

# For loop in Tuple
my_tuple = (1,2,3,4)
for i in my_tuple:
    print(i)

# For loop in String
my_string = "Hello"
for i in my_string:
    print(i)
    

# For loop for Tuples inside a list (First Method)
my_list = [(1,2),(3,4),(5,6)]
for i in my_list:
    print(i)

# For loop for Tuples inside a list (2nd Method - Getting both values )
my_list = [(1,2),(3,4),(5,6)]
for a,b in my_list:
    print(a,b)
    
    
# For loop in Dictionary            (Outputs both Keys and Values)
my_dict = {"name":"rohit","age":"34"}
for a,b in my_dict.items():
    print(a,b)

# For loop in Dictionary            (Output only Keys )
my_dict = {"name":"rohit","age":"34"}
for i in my_dict.keys():
    print(i)
    
# For loop in Dictionary            (Outputs only Values )
my_dict = {"name":"rohit","age":"34"}
for i in my_dict.values():
    print(i)

