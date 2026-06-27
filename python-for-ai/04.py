'''
add = lambda x,y : x+y
print(add(22,34))

while True:
    num = int(input("Enter a number to check if its true or false(0 to leave) - "))
    if num == 0 :
        print("Exited successfully!")
        break
    else :
        even_odd = lambda x : "Even" if x % 2 == 0 else "Odd"
        print(f"Your {num} is {even_odd(num)} number!")

'''
#-----------------------------------------------------------------------------------------------------------

from name import greet
import math


math.sqrt(5)
math.asin(1)
name1 = input("Please enter your name -")
greet(name1)

print(help(math))


#-------------------------------------------------------------------------
        #Task 4 
#-------------------------------------------------------------------------


#Q1. (Lambda Function)

square = lambda x : x ** 2 

num1 = int(input("Enter a number to find it's Square - "))

print(f"The square of the number {num1} is {square(num1)}")

def square_function(x):
    print(f"The square of {x} is - {x **2} ")
num2 = int(input("Enter a number to find it's Square - "))
square_function(num2)


""" The normal function takes the input and either returns it manually
or prints it within itself, it also has it's own name and is called 
by the programmers using it's function name.
Whereas, the lambda function is an anonymous function that directly 
returns the value of the function that is stored in a variable and 
thus this variable is used to call it.
"""


#-------------------------------------------------------------------------
#Q2. (Lambda with Multiple Arguments)

add_three = lambda a,b,c : a + b + c 

num1 = int(input("Enter the first number - "))
num2 = int(input("Enter the second number - "))
num3 = int(input("Enter the third number - "))

print(f"The addition of this three numbers is - {add_three(num1,num2,num3)}")

#-------------------------------------------------------------------------

#Q3. (For Loop Revision)

#a -
for i in range(1,26) :
    print(i)

#b -
sum = 0
for i in range(1,21) :
    sum = sum + i

print(sum)


#-------------------------------------------------------------------------

#Q4. (While Loop Revision)
while True:
    num = int(input("Enter a positive number(stops when 0 or negative number is detected-) "))
    if num <= 0 :
        print("Program Terminated!")
        break
    else :
      sum += num 

print(f"The addition of the given numbers is - {sum}")

#-------------------------------------------------------------------------

#Q5. (Math Module)

import math # allows us to do various math operation effortlessly using it's functions

number = float(input("Enter any number -"))

print(f"Its Square root is - {math.sqrt(number)}")

if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number.is_integer():   # factorial only works for integers
    print(f"Its factorial is - {math.factorial(int(number))}")
else:
    print("Factorial is only defined for integers.")

print(f"Its ceiling value is - {math.ceil(number)} and its floor value is -  {math.floor(number)}")

#-------------------------------------------------------------------------

#Q6. (Random Module)

import random

print("The 5 random numbers generated between 1 and 100 are -")
for i in range(6):
    print(random.randint(1,100))

print(F"One random number between 50 & 150 is - {random.randint(50,150)}")

print(F"One random floating number between 0 & 1 is - {random.random()}")




#-------------------------------------------------------------------------

#Q7. (Import Methods)

import math #imports entire math module
print(f"The base of 2 to the power 4 is - {math.pow(2,4)}")

from math import sqrt #imports only sqrt()
print(f"The square root of 4 is - {sqrt(4)}")

import math as m #used m as an ally 
print(f"The factorial of 5 is - {m.factorial(5)}")

#-------------------------------------------------------------------------

#Q8. (Custom Module) and Q9. (name == "main")

import mymodule

mymodule.greet("Pranav")

power = mymodule.calculate_power(2,4)
print(f"The power of 2 ^ 4 is - {power}")


#The file didnt run the test code due to the condition - if __name__ == "__main__"
#-------------------------------------------------------------------------

#Q10. (Mini Project - Combined Concepts)

#Simple Math Utility Program

import math 
import random 

square = lambda x : x ** 2 #calculates and returns the square 

def power(base,exp):
    print(f"The power of {base} to {exp} is - {math.pow(base,exp)} ")

while True:
   
    choice = input("Enter what you want to do - (Square,Power,Random Number or Exit)").lower()       
    if choice == "exit" :
        break
    elif choice == "square" :
        number = int(input("Enter a number to perform squaring -"))
        print(f"The square of the {number} is - {square(number)}")
    elif choice == "power" :
        base = int(input("Enter the base - "))
        exp = int(input("Enter the exponent -"))
        power(base,exp)
    elif choice == "random number" :
         print("We will choose any random number for you!")
         print(f"The random number is - {random.randint(0,9)}")
    else :
         print("Square,Power,Random Number")
         print("Only enter the above mentioned choice ")
