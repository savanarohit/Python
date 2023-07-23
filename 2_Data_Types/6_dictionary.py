# Python Data Type - Dictionary

# Sample Dictionary 
my_dict = {
    "name":"Savana",
    "age":"34",
    "board": "cbse",
    }

print(my_dict)

# Dictionary Keys data type
print(type(my_dict['name']))
print(type(my_dict['age']))
print(type(my_dict['board']))

# Updating a Dictionary
my_dict = {
    "name":"Savana",
    "age":"34",
    "board": "cbse",
    }

my_dict2 = {
    "name":"Rohit",
    "age":"35",
    "board":"icse"
}

my_dict.update(my_dict2)
print(my_dict)

# Dictionary Items
final=my_dict.items()
print(final)

# Dictionary Values
final=my_dict.values()
print(final)

# Dictionary Keys
final=my_dict.keys()
print(final)