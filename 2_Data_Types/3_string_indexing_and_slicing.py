# String Indexing - Using [N] Where N is Indexing value . Index starts with 0

# Using index value
my_name = "Rohit"
demo = my_name[0]
print(demo)
demo = my_name[1]
print(demo)

# Combining two strings using + 
first_name = 'Savana '
last_name = 'Rohit'

full_name = (first_name + last_name)
print(full_name)


## String Slicing -  Using [0:N] Where N is the string index value

# Using Index Value in [0:] (Start from 0 and till the end)
my_name = 'Savana'
name = my_name[0:]
print(name)

# Using Index Value [0:3] (Start from 0 and end till the 3rd Index)
name = my_name[0:3]
print(name)

# Using Index Value [0:4:2] (Start from Index -0 till 4th Index , jump 2 position in between 0 to 6 )
my_string = 'Hello World'
name = my_string[0:10:2]
print(name)

# Using Negative Index Value
name = my_name[-1]
print(name)

# Using Negative Index Value [-0:] (Start from -0 and till the end)
name = my_name[-0:]
print(name)

# Using Negative Index Value [-0:] (Start from Index -0 then jump to 4th Index and 2 )
my_string = 'Hello World'
name = my_string[0:10:2]        # (0: is starting point and 10 is ending , 2 is jump value)
print(name)

