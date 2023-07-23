# Data Type Task

# 1. write a program to get length of a string
my_str = "Rohit"
output = len(my_str)
print(output)

# 2. write a program to print first and last of a list
my_list = [1, 2, 3, 4]
output1 = my_list[0]
output2 = my_list[-1]
print(output1)
print(output2)

# 3. For a dict my_dict = {"name":"abc","list":[1,2,3]} print length of list , print first index of list
my_dict = {"name": "abc", "list": [1, 2, 3]}

output1 = len(my_dict["list"])
print(output1)

my_list = my_dict["list"][0]
print(my_list)

# 4. If a=  3 + 1.5 + 10. What is the type of a ?
a = 3 + 1.5 + 10
print(type(a))

# 5. If a = [1,2,3,[1,2,"name"]]. replace name with gender
a = [1, 2, 3, [1, 2, "name"]]
output = a[3]
print(output)

# Since list is mutable then replace value with gender
my_list = a[3][2] = "gender"
print(my_list)

# 6. If a ={"name":"test","gender":23,"demo":[1,2,3,[1,2,3,"name"]]}. replace name with gender
a = {"name": "test", "gender": 23, "demo": [1, 2, 3, [1, 2, 3, "name"]]}
print(a)

demo = a["demo"][3][3] = "gender"
print(a)

# 7. If a = {"a1":[{"a2":["i am a string",["grab me"]]}]}. print grab me
a = {"a1": [{"a2": ["i am a string", ["grab me"]]}]}
output = a["a1"][0]["a2"][1]
print(output)

# 8. What is major difference b/w list and tuple?
# List is Mutable and Tuple is Immutable

# 9. What is a set?
# Set stores only unique objects in a sequence

# 10. 3.0 == 3. True or False?
print(3.0 == 3)  # True

# 11. 3 <= 3 < 4 > 1 < 5 >= 5. True or False?
print(3 <= 3 < 4 > 1 < 5 >= 5)  # True

# 12. let a =  [1,2,3,{"a":[{"age":24}]}] and b = {"age":[{"age":20}]} grab both ages and then check if both are equal
a = [1, 2, 3, {"a": [{"age": 24}]}]
b = {"age": [{"age": 20}]}

output1 = a[3]["a"] == b["age"][0]
print(output1)

output2 = a[3]["a"][0]["age"] == b["age"][0]["age"]
print(output2)
