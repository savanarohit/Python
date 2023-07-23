# Pass - Do nothing for loop

my_list = [1,2,3,4]
for item in my_list:
    pass

# continue - without using continue
for i in my_list:
    if i == 1:
        # continue
        print(f"Number inside the for loop")
    else:
        print(f"Number inside the else loop is:",i)


# continue - with using continue
for i in my_list:
    if i == 1:
        continue
        print(f"Number inside the for loop")
    else:
        print(f"Number inside the else loop is:",i)
        
# break - exit a loop
for i in my_list:
    if i == 4:
        break
    else:
        print(f"Number in for loop is:",i)