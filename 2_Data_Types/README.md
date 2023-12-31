### Python Data Types

1. Integers (Numbers - 0 , -1 , -2 )

    roll_number = 100 <br>
    print(roll_number)

    Python representation of Integers
    Type: int
    name: integer

2. Decimal (Floating - 0.2 , 1.4 )

    my_float = 1.2 <br>
    print(type(my_float))

    Python representation of Decimal
    Type: float
    name: floating point

3. String ("hello") - String is sequence of characters below all are characters

    my_string = 'Hello' <br>
    print(my_string) <br>
    print(type(my_string))

    Python representation of String <br>
    type: str <br>
    name: String

4. Boolean (True or False) - Logical Value telling if a condition is True or False

    my_bool1 = True <br>
    my_bool2 = False

    if my_bool1 == my_bool2: <br>
        print("True") <br>
    else: <br>
        print("False")

    Python representation of Boolean <br>
    type: bool <br>
    name: boolean

5. List ( ["Values"] ) - List is a Ordered Sequence (It can contain any data types integer , string , float etc)

    mylist = [ 1,2,"hello",4.2] <br>
    print(mylist)

    Python representation of List <br>
    type: list <br>
    name: List

6. Dictionary ( {"name:" "rohit" , "age:" "34" } ) - Unordered Sequence of Key & Value Pair Sequence separated by ,

    my_dict = {"name:" "Savana" , "age:" "34"} <br>
    print(my_dict)

    Python representation of Dictionary <br>
    type: dict <br>
    name: Dictionary

7. Tuples ( ) - Ordered immutable (cannot be changed ) Sequence separated by ,

    my_tuple = (1,2,"hello") <br>
    print(my_tuple)

    Python representation of Tuples <br>
    type: Tuples <br>
    name: Tuples

8. Sets { 1 , 2 , 3 } - Unordered collection of unique objects Sequence separated by ,

    my_set = {1,2,3,1,4} <br>
    print(my_set)

    Python representation of Sets <br>
    type: sets <br>
    name: Sets

9. Variables

    Variable - Variable is a reference to store information

    my_var = 10

10. Rules to assign a variable name

    a. There should be no space between a Variable <br>
    b. We cannot use special symbols in name like #$@ 

11. Best practice while assign a variable name

    a. Use lower case only - my_name <br>
    b. You should not use Python Keywords like : list , str , bool etc

12. Troubleshooting errors while learning python

    a. First try to debug  (Syntax error , Logical error etc) <br>
    b. Google the errors

13. BODMAS (Brackets, Order, Division and Multiplication, Addition and Subtraction)

    BODMAS stands for "Brackets, Order, Division and Multiplication, Addition and Subtraction," and it is a rule used in mathematics and programming to determine the sequence of operations when evaluating mathematical expressions.

    Brackets ()                          (Anything within parentheses is evaluated first)

    result = (2 + 3) * 4 <br>
    print(result)  # Output: 20

    Order **                             (Exponents are evaluated next)

    result = 2 ** 3 <br>
    print(result)  # Output: 8

    Division & Multiplication / & *      (Next but same level of precedence)

    result = 4 * 2 / 3 <br>
    print(result)  # Output: 2.6666666666666665

    Addition & Subtraction  + & -        (Last but same Level of precedence)

    result = 10 - 3 + 2 <br>
    print(result)  # Output: 9

