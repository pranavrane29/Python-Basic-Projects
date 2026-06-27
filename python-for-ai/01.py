print('Hello world')
doxstream = ''' here we store the multiple 
strings into the string variable
''' 
#we can store the string data in single , doouble and triple quotes.

bool = False
is_verified = bool

numbers[10] = {1,2,3,4,5,6,7,8,9,10}

#studied various aritmetic operators like + - * / // % 

is_equal = 3 != 3.0

age = input("Enter your age -")
age = int(age)

name = "Pranav"
name[0] = "B" 

name.replace("P","B")



#----------------------------------------------------------------------------------
                            # Task 1
#----------------------------------------------------------------------------------     

#Q1. Variables & Naming Rules

name = "Pranav Gajanan Rane"
age = 18
height = 1.68 #in meters ~ 168cm
is_student = True

print(f"My name is - {name}")
print(f"I am {age} years old")
print(f"My height is - {height}")
print(f"Am I a Student - {is_student}")

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

'''
The names for the variables are choosen based on 
what i had to store in the variable
''' 
#----------------------------------------------------------------------------------

#Q2. Data Types

name = "Stores String" # Datatype --> str
age = 27 # Datatype --> int
percentage = 91.25 # Datatype --> float
can_vote = True # Datatype --> bool


print(type(name))
print(type(age))
print(type(percentage))
print(type(can_vote))

age = float(age) #converts int to float
percentage = int(percentage)  #converts float to int

print(age)
print(percentage)

#----------------------------------------------------------------------------------

#Q3.Operators - Arithmetic

a = 15
b = 4

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floor_divison = a // b
modulo = a % b
exponent = a ** b 

print(f"Addition - {addition}")
print(f"Subtraction - {subtraction}")
print(f"Multiplication - {multiplication}")
print(f"Division - {division}")
print(f"Floor Division - {floor_divison}")
print(f"Modulo - {modulo}")
print(f"Exponentiation - {exponent}")

'''
The difference between / and // is - 
--> division(/) = performs normal division and gives the decimal value 
if the answer is so
--> floor_divison(//) = also performs the divison but do not give the decimal value
ex - 5/3 gives us 1.666
but 5//3 gives us only the whole integer part i.e 1 and omits the decimal part .666'''

#----------------------------------------------------------------------------------

#Q4.Operators - Comparison & Logical

x = 25
y = 30 
z = 25

print(x > y ," --> NO,x is not greater than y")
print(x == z, "--> Yes,x is equal to z")
print((x <= y) and (y != z), " --> Yes, x is less than or equal to y AND y is not equal to z")
print((x > y) or (x == z), " --> Yes,x is greater than y OR x equals z")

#----------------------------------------------------------------------------------

#Q.5 Input/Output

name = input("Enter your name - ")
year = int(input ("Enter your birth year - "))
current_year = 2026

age = current_year - year
print(f" Your current age is - {age}")

'''
we needed to convert the input to integer because 
the input() only accepts the input in the string format therefore
we need to typecast the input into the Integer format so that 
arithmetic operation can be done on it
'''

#----------------------------------------------------------------------------------

#Q.6 Combined - Variables, Operators & Input

height = float(input("Enter your height(in meters) -")) #takes height as input
weight = float(input("Enter your weight(in kg) - "))  #takes weight as input
BMI = weight / (height ** 2)# calculates here 

BMI = round(BMI, 2) # rounds of to 2 decmial places 

print(f"Your BMI is - {BMI}") # Displays the BMI

#----------------------------------------------------------------------------------

#Q.7 Comments

# Program to calculate the area and perimeter of the rectangle 

length = float(input("Enter the length of the rectangle - ")) #Takes length as an input 
width = float(input("Enter the width of the rectangle - ")) #Takes width as an input 

"""
We used typecasting here as we took the floating type of values from the user
"""
area = width * length #Calculates the Area
perimeter = 2 * (length+width) #Calculates the Perimeter

print(f"The area of the rectangle is - {area}") #Displays the Area
print(f"The perimeter of the rectangle is - {perimeter}") #Displays the Perimeter

'''
This program takes input of length and width from the user 
and calculates the area and rectangle for the rectangle and 
prints the output
'''

#----------------------------------------------------------------------------------

#Q.8 Operators - Assignment & Membership

fruits = ["mango", "apple", "banana", "cherry"]
score = 50

score += 25
print(f"Updated score is - {score}")


if "apple" or "Apple" in fruits :
    print("Apple is in the list")
else :
    print("Apple is not in the list")

if "grape" or "Grape" not in fruits :
    print("Grape is not in the list")
else :
    print("Grape is in the list")


#----------------------------------------------------------------------------------

#Q.9 Mini Project - All Concepts

#Student Profile Generator

name = input("Enter your Full Name - ")
age = int(input("Enter your age - "))
city = input("Enter the name of your city - ")

print("Enter your marks in 3 subjects - ")

subject_1 = int(input("Enter marks of Maths - "))
subject_2 = int(input("Enter marks of Science - "))
subject_3 = int(input("Enter marks of English - "))

total_marks = subject_1 + subject_2 + subject_3
percentage = (total_marks/300) * 100

#Profile displaying --

print("Student Profile --")

print(f"Student Name - {name}")
print(f"Student Age - {age}")
print(f"Student's City - {city}")

print("Students Marks in 3 subjects -")

print(f"Maths - {subject_1}")
print(f"Science - {subject_2}")
print(f"English - {subject_3}")

print(f"Their total marks are - {total_marks}")
print(f"Their Percentage is - {percentage}")

print("-" * 60)
print("Thank you visiting the Student profile")

#----------------------------------------------------------------------------------

#Q.10 Debugging and Understanding 

'''
'''Wrong Code - '''

Name = "Alice" #correct 

age 20 # missing the assignment operator

city = Amsterdam #missing string declaration

print("My name is" + Name) #needs proper spacing 

print("I am" age "years old") # missing f string concept 

print("I live in " city) # missing the + operator after the statement

# Check if age is greater than 18 and print message
print("Adult:" age > 18)# missing the comma(,) after the statement
'''

'''Corrected Code - '''

Name = "Alice"
age = 20
city = "Amsterdam"
print("My name is " + Name)
print(f"I am {age} years old")
print("I live in ", city)
# Check if age is greater than 18 and print message
print("Adult:", age > 18)