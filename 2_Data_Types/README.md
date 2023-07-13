# Python Data Types

## Integers (Numbers)

1. Integers (0 , -1 , -2 )

## Python representation of Integer
Type: int
name: integer

2. Decimal (0.2 , 1.4 )

# Python representation of Decimal
Type: float
name: floating point

3. String  ( "hello" )

String is Sequence of characters Below all are characters , when combined it will become a string.

"H"     "E"     "L"     "L"     "O"

string = "Hello"

# Python representation of String
type: str
name: String

4. Boolean ( True or False )

Logical Value telling if a condition is True or False

# Python representation of Boolean
type: bool
name: boolean


5. List ( ["Values"] )

List is a Ordered Sequence (It can contain any data types integer , string , float etc)

How to write a list ?

[ 1,2,"hello",4.2]

# Python representation of List
type: list
name: List

6. Dictionary ( {"name:" "rohit" , "age:" "34" } )

Unordered Sequence of Key & Value Pair Sequence separated by ,

{"name:" "Savana" , "age:" "34"}

# Python representation of Dictionary
type: dict
name: Dictionary

7. Tuples ( )

Ordered immutable (cannot be changed ) Sequence separated by ,

(1,2,"hello")

# Python representation of Tuples
type: Tuples
name: Tuples

8. Sets { 1 , 2 , 3 }

Unordered collection of unique objects Sequence separated by ,

{}

# Python representation of Sets
type: sets
name: Sets


## Variables

Variable - Variable is a reference to store information

# Rules to assign a Variable in Python

1. There should be no space between a Variable
2. We cannot use special symbols in name like #$@ 

# Best practice while assign a name

1. Use lower case only - my_name
2. You should not use Python Keywords like : list , str , bool etc

# How You should proceed if you get errors while learning python ?

1. First try to debug  (Syntax error , Logical error etc)
2. Google the errors

## BODMAS

BODMAS stands for "Brackets, Order, Division and Multiplication, Addition and Subtraction," and it is a rule used in mathematics and programming to determine the sequence of operations when evaluating mathematical expressions.

1. Brackets ()                          (Anything within parentheses is evaluated first)

result = (2 + 3) * 4
print(result)  # Output: 20


2. Order **                             (Exponents are evaluated next)

result = 2 ** 3
print(result)  # Output: 8


3. Division & Multiplication / & *      (Next but same level of precedence)

result = 4 * 2 / 3
print(result)  # Output: 2.6666666666666665


4. Addition & Subtraction  + & -        (Last but same Level of precedence)

result = 10 - 3 + 2
print(result)  # Output: 9

