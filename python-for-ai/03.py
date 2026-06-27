'''
def multiply(a,b) :
    return a * b

num1 = float(input("Enter the first number - "))
num2= float(input("Enter the second number - "))

multiply = multiply(num1,num2)


print(multiply)

#-------------------------------------------------------------------------


Create a Simple Number Analyzer program using functions:
1. get_number() → takes input from user and returns the number.
2. is_even(num) → returns True if number is even, else False.
3. power(base, exp=2) → returns base raised to exponent (use default argument).
4. show_result(num) → prints whether the number is even/odd and its square.
Use a while loop to repeatedly ask the user for numbers until they enter 0.
Use recursion only if needed for one small part.
'''

def get_number() :
    return int(input("Enter a number - "))

def is_even(num) :
    if num % 2 == 0 :
        print("The number is even")
    else : 
        print("The number is odd")

def power(base, exp = 2) :
    exp = int(input("Enter to the power you want to find- "))
    return base ** exp 

def show_result(num):
     is_even(num)
     print("The power of the given number is - ",power(num))

while True :
    
    num = get_number()
    if num == 0:
        print("Enter only positive number idiot!!")
        break 

    show_result(num)


#----------------------------------------------------------------------------------

#Q1. (Basic Function)

def welcome() :
    print("Welcome to Python Programming!")

welcome()

'''
Functions are useful because they make the program
more structured and also avoid unnecessary repetation
of a specific program(statement)'''

#----------------------------------------------------------------------------------

#Q2. (Function with Parameter)

def greet(name) :
    print(f"Hello, {name}! Welcome back.")

greet("Pranav") #my own name 
greet("Gauri") #other name (reusability)

#----------------------------------------------------------------------------------

#Q3. (Default Parameter)

def show_message(message = "Hello") :
    print(message)

show_message()
show_message("Mountreach")

'''
passing default arguments helps us to pass a default value
the the local varibles when no other argument is given'''

#----------------------------------------------------------------------------------

#Q4. (Function with Multiple Parameters & Return)

def calculate_sum(a,b) :
    return a + b

result = print(calculate_sum(4,3))

'''Above we can see that the function returns a value and 
we store it in our variable to print it. Either we can do this, or 
else what we can do is that we directly print the value in the function itself instead of 
asking it for a value . Example -
def add(a,b):
    print(a + b)
    
now whenever we call this function, instead of returning the 
value, it directily prints it '''

#----------------------------------------------------------------------------------

#Q5. (Positional vs Keyword Arguments)

def student_info(name,age) :
  print(f"Hello,{name}")
  print(f"You're {age} years old!")

g_name = 'Pranav'
g_age = 18
student_info(g_name,g_age) #positional arguments 
student_info(age=19,name="Gauri")# keyword arguments

'''Positional arguments - values are assigned to parameters based on their order/position in the function call. Python matches left to right.
Keyword arguments - values are assigned by explicitly naming the parameter in the function call. Order does not matter.'''

#----------------------------------------------------------------------------------

#Q6. (Function with Return Value)

def square(num) :
    return num ** 2

def cube(num) :
    return num ** 3

g_num = int(input("Enter a number to find its square and its cube -"))

print(f"The square of {g_num} is - ", square(g_num))


print(f"The cube of {g_num} is - ", cube(g_num))

#----------------------------------------------------------------------------------

#Q7. (Recursion - Basic)

def countdown(n) :
    if n <= 0 : 
        return #base case 
    else :
        print(n)
        countdown(n-1) #recursive case


countdown(10)

#----------------------------------------------------------------------------------

#Q8. (Recursion - Factorial)

def factorial(n) :
    if n <= 1 : #base case stops recursion because factorial of 1 is 1 
        return 1
    else :
       return n * factorial(n-1)

g_num = int(input("Enter the number to find it's factorial -"))

print(factorial(g_num))

#----------------------------------------------------------------------------------

#Q9. (Scope - Local vs Global)

total = 0

def add_value(x) :
    global total
    total = total + x
    print(total)
    a = 5 #local variable

add_value(4)
add_value(6)
add_value(1)
add_value(9)
add_value(8)
add_value(7)


# print(a) --> creates an name error --
'''NameError: name 'a' is not defined'''


#----------------------------------------------------------------------------------

#Q10. (Mini Project - All Concepts)

#Simple Number Analyzer

def get_number() :
    num = int(input("Enter any number to get its square and cube (0 to exit)-"))
    return num

def is_even(num) :
    if num % 2 == 0 :
       return True
    else :
        False

def power(base, exp = 2) :
    return base ** exp

def show_result(num) :
    global g_num
    if is_even(num) == True :
        print(f"{num} is an even number")
    else :
        print(f"{num} is an odd number")

    pow = power(g_num)
    print(f"The square of the given number is - {pow}")

while True :
    g_num = get_number()
    if g_num == 0:
        break
    else :
        show_result(g_num)

