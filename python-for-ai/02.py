'''

if a == 10 :
    print("Hello")
elif a > 10 :
    print("Bye")
else :
    print("Exititng")


name = input("Enter the admin name -")
age = int(input("Enter your age -"))


if (name == "Pranav" or "Gauri" or "Pari" ) and age >= 18 :
    print("You are eligible to enter the app!")
    print("Enter the password to confirm your login -")

else :
    print("You are not allowed to log in!")

pass_key = input("Password - ")
if pass_key== "Gaurishankar@143" :
        print("Logged in!!")
else :
        print("Wrong password, try again!")

'''


#----------------------------------------------------------------------------------
                            # Task 2
#----------------------------------------------------------------------------------           


#Q1. (if Statement)

# Program to check if you are eligible to vote

age = int(input("Enter your age - ")) #inputs the age

if age >= 18 :  #checks the condition and prints if true
    print("You are eligible to vote!")


#----------------------------------------------------------------------------------

# Q2. (if-else Statement)

# Program to check even / odd numbers
number = int(input("Enter a number to determine if its true or false - "))

if number % 2 == 0 :
    print(f"{number} is an Even Number.")
else :
    print(f"{number} is an Odd Number.")


#----------------------------------------------------------------------------------

#Q3. (if-elif-else Statement)

marks = int(input("Enter your marks to determine your grade -"))

if marks >= 90 :
    print("Grade A -> Excellent")
elif marks >= 75 :
    print("Grade B -> Good")
elif marks >= 60 :
    print("Grade C -> Average")
elif marks >= 40 :
    print("Grade D -> Pass")
else :
    print("Fail")


#----------------------------------------------------------------------------------

#Q4. (For Loop with range)

#Print all numbers from 1 to 30. 
for num1 in range(1,31) : #prints from 1 to 30 numbers
    print(num1)

#Print all odd numbers from 1 to 50.
for num2 in range(1,51) : #prints from 1 to 50 numbers
    if num2 % 2 != 0 :
        print(num2) 
    
# Print the sum of numbers from 1 to 15.
temp = 0
for num3 in range(1,16) : #prints from 1 to 15 numbers
    temp += num3 
print(temp)

'''
The basic work of range() is that it generates the iterators.
It has 3 main types -
i)range(stop)
ii)range(start,stop)
iii)range(start,stop,leap by)
The loop will always run till stop - 1'''


#----------------------------------------------------------------------------------

#Q5. (While Loop)

#print numbers from 1 to 20
i = 1
while i <= 20 :
    print(i)
    i = i + 1

#Also print the cube of each number (i.e., 1³, 2³, 3³, ...).

i = 1
while i <= 20 :
    print(i ** 3)
    i = i + 1


#----------------------------------------------------------------------------------

#Q6. (While Loop - User Controlled

sum = 0

while True:
   
    user_input = int(input("Enter a positive number - "))
    
    if user_input <= 0:
        break #if condition becomes true, we exit the loop
        
    sum += user_input

print(f"The total sum of all entered positive numbers is: {sum}")


#----------------------------------------------------------------------------------


#Q7. (Nested if Statement)

temperature = int(input("Enter the temperature outside - "))
is_raining = input("Enter Yes or No - ")

if temperature > 30 :
    if is_raining == "No" :
     print("Hot day, wear light clothes")
    else:
        print("Hot and rainy, carry umbrella")
elif temperature < 15 :
    if is_raining == "Yes" :
        print("Cold and rainy, wear jacket and take umbrella.")
    else :
        print("Cold, wear a jacket")
else :
    print("Enter only Yes or No specifically. ")

#----------------------------------------------------------------------------------

#Q8. (For Loop + if-elif-else)

for i in range(1,41) :
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 :
         print("Fizz")
    else :
        print(i)

#----------------------------------------------------------------------------------

# Q9. (Menu Driven Program)

while True :
    print("Welcome to calculator!")

    operator = input("Select the task you want to perform (+,-,*,/) or press 5 to exit -")
    
    if operator == "5" :
        print("Successfully exited the calci.")
        break

    num1 = int(input("Enter the first number -"))
    num2 = int(input("Enter the second number -"))

    if operator == "+" :
        add = num1 + num2 
        print(f"The addition of {num1} and {num2} is - {add}")
    elif operator == "-" :
        sub = num1 - num2
        print(f"The subtraction of {num1} and {num2} is - {sub}")  
    elif operator == "*" :
        multiply = num1 * num2 
        print(f"The multiplication of {num1} and {num2} is - {multiply}")
    elif operator == "/" :
        if num2 == 0 :
            print("Cannot divide by 0")
        else :  
            div = num1 / num2
            print(f"The division of {num1} and {num2} is - {div}")  


#----------------------------------------------------------------------------------

#Q10. (Debugging)


#wrong code -
num = input("Enter a number: ")  #should typecast to int
if num > 100  #missing :
    print("Large number")  
elif num > 50   #missing :
    print("Medium number")
else
    print("Small number")

count = 1
while count < 10 #missing :
    print(count) #wrong indentation
    count + 1 #wrong operator used 


# Corrected code
num = int(input("Enter a number: "))
if num > 100 :
    print("Large number")
elif num > 50 :
    print("Medium number")
else :
    print("Small number")

count = 1
while count < 10 :
    print(count)
    count += 1

fruits = ["apple", "banana", "orange"]

for fruit in fruits :
    print(fruit)


times_we_run = int(input("How many times do you want to print Hello?"))

while times_we_run > 0 :
    print("Hello")

    times_we_run -= 1

    