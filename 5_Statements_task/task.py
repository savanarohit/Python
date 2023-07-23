# Statement Task

# 1 - Let a = [1,2,3,4,5] use a for loop and print all odd and even numbers separately.
a = [1,2,3,4,5]
for i in a:
    if i % 2 == 0:
        print("The number is even:",i)
    else:
        print("The number is odd:",i)
  
# Let a = [1,2,3,4,5,6] then get a list b. which contains all even number from list a. example, List b should look like this. b = [2,4,6]

# Use List comprehension
a = [1,2,3,4,5,6]
b = [i for i in a if i % 2 == 0] 
print(b)

# 3 - take a range of numbers (0,50) and print ‘haha’ for numbers which are multiple of 3. print ‘hehe’ for numbers which are multiple of 5. print ‘heha’ for numbers which are multiple of both 3 and 5. print numbers which are neither multiple of 5 nor multiple of 3.
for i in range(0,50):
    if i % 3 == 0 and i % 5 == 0:
        print("heha")
    elif i % 3 == 0:
        print("haha")
    elif i % 5 == 0:
        print("hehe")
    else:
        print(i)

# 4 - for a range (0,50). if a number is less than 10 do nothing. if greater than 10 print number print it. but if number equal to 30 exit the loop.
for i in range(0,50):
    if i < 10:
        pass
    elif i == 30:
        break
    else:
        print(i)
    
# 5 - for number starting from 0-10 (include 10 also). print average of these numbers. Do it using for loop and while loop both.

# Using for loop
sum = 0
for i in range(0,11):
    sum = sum + i
print(sum/10)

# Using while loop
i = 0
sum = 0
while i < 11:
    sum = sum + i
    i = i + 1
print(sum/10)
    
# 6 - Take range (0,20) and create a list of square of  all odd numbers.
list = [i**2 for i in range(0,20) if i % 2 != 0]
print(list)
    
#  7 - Take value of length and breadth from user and then check whether it is square or rectangle. also print it.
length = input("Enter length: ")
breadth = input("Enter breadth: ")
if length == breadth:
    print("It is a Square")
else:
    print("It is a rectangle")

# 8 - Let say a school has following grade system.
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Now ask user to enter his int(marks) and print his grade accordingly.

(marks) = int(input("Please enter your mark to know your grade"))
if int(marks) < 25:
    print("Grade F")
elif 25 <= int(marks) < 45:
    print("Grade E")
elif 45 <= int(marks) < 50:
    print("Grade D")
elif 50 <= int(marks) < 60:
    print("Grade C")
elif 60 <= int(marks) < 80:
    print("Grade B")
else:
    print("Grade A")

# 9 - Student won’t be allowed to sit in exam if his/her attendance is less than 75%. Ask student to give no of class he has attended then print if he is eligible to sit in exam or not.Total number of classes are 50 .If student enter attended class more than 50 then print you are lying.  

total_classes = 50
attended_classes = input("Enter no of classes you have attended: ")
percentage = float(int(attended_classes)/total_classes) * 100
print("Percentage is: ", percentage)

if int(attended_classes) > 50:
    print("You are lying")
elif percentage > 75:
    print("You are eligible for exam: ")
else:
    print("You are not eligible for exams: ")
