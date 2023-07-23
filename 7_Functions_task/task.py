# Function task

# 1 - Write a function which take any number of arguments of type number and return a list only with even numbers. 
def even_num(*args):
    return list(filter(lambda x : x % 2 == 0,args))

output = even_num(1,2,3,4,5,6,7,8,9,10)
print(output) 

# 2 - Write a function which takes 3 argument number, low , high. Return whether the given number is between the range or not. low means: starting of range. high means: end of range
def is_num_in_range(number,low,high):
    return number in range(low,high)

print(is_num_in_range(5,0,4))
print(is_num_in_range(2,0,4))

# 3 - Write a function which takes a string and print number of uppercase letters and num-ber of lower case letters in that string
def count_case(string):
    lower_case = 0
    upper_case = 0
    for letter in string:
        if letter.isupper():
            upper_case += 1
        else:
            lower_case += 1
            
    return {"lower_cae":lower_case, "upper_case":upper_case}
 
output = count_case("This is a Demo of Hello World!")
print(output)

# 4 - Write a function which take a list and return a new list of unique numbers. example - list a = [1,2,3,3,1,1,4,5]  output = [1,2,3,4,5]
def unique_list(*args):
    unique_list = []        # Empty list
    for number in args:
        if number not in unique_list:
            unique_list.append(number)
    return(unique_list)

output = unique_list(1,2,3,4,4,1,1,2,3,3)
print(output)