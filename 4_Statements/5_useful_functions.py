# Python Useful Functions

# range
for i in range(10):
    print(i)

# range - start and end
for i in range(2,5):
    print(i)
    
# range - start , end and jump position by n number
for i in range(2,10,2):
    print(i)
    

# increment by 1
count = 0
my_string = "Hello"

for l in my_string:
    print(f"My index is {count} and letter is: {l}")
    count += 1
    
# Decrement by 1
count = 0
my_string = "Hello"

for l in my_string:
    print(f"My index is {count} and letter is: {l}")
    count -= 1   
    
    
# Enumerate - Rather than using above method use this
count = 0
my_string = "Hello"
for l in enumerate(my_string):
    print(l)

# zip 
my_list1 = [1,2,3,4]
my_list2 = [5,6,7,8]

for i in zip(my_list1,my_list2):
    print(i)
    
    
# in
string_check = 'x' in [1,2,3]
print(string_check)

number_check = 1 in [1,2,3]
print(number_check)

# min and max
my_list = [1,2,3,4,5]
print(min(my_list))
print(max(my_list))


# user input
user_name = input("Enter your name: ")
print(f"Your name is:", user_name)