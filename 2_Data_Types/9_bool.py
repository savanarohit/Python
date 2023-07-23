# Python Data Type - boolean

# 0      => False
# > 0    => True

# Sample bool (True or False)
my_bool1 = True
my_bool2 = False

if my_bool1 == my_bool2:
    print("True")
else:
    print("False")

# Example
n = 10
result = n == 11        # Since 10 is not Equal to 11 it will print False
print(result)

# in condition          # Sine both name and output are same - True
name = "Savana"
output = "Savana" in name
print(output)

# not in                # Sine both name and output are different - False
name = "Savana"
name= "Savana"
output= "Savana" not in name
print(output)

# Condition
num = 10
output = num > 5
print(output)

output = num < 20
print(output)

# 0     => False
# >0    => True
my_bool = not bool(0)
print(my_bool)

