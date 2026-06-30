#----------------------------------------------------------------------------------------------------------
                # Task 12th
#----------------------------------------------------------------------------------------------------------

'''I use Jupyter server to run code one by one, so i do not concern myself with duplicate
variables and all so pls take a note that running the entire code may cause error! '''


#----------------------------------------------------------------------------------------------------------

#Q2. (Strings + Loops + Functions)

def analyze_string(s) :

    if s == "":
        print("Empty string entered. Please enter a valid string!")
        return
     
    print(f"The length of the entered string is - {len(s)}")

    print(f"The reverse of the given string is - {s[-1::-1]}") # Prints in reverse order

    vowels = "aeiou"        
    count = 0  
    for i in s:
        if i.lower() in vowels :
            count +=1 

    print(f"Vowles count is - {count}")

    print("String with its positive indices")
    index = 0
    for i in range(len(s)) :
        print(f"{s[i]} at index - {index}")
        index += 1

    print("String with its negative indices")
    index = -1
    for i in range(-1,-len(s)-1,-1) :
        print(f"{s[i]} at index - {index}")
        index -= 1


string = input("Enter a string - ")
analyze_string(string)


#----------------------------------------------------------------------------------------------------------

#Q3. (Lists + Functions + Exception Handling)

def manage_marks() :
    try :    
        mark1 = int(input("Enter your marks in subject 1 - "))
        mark2 = int(input("Enter your marks in subject 2 - "))
        mark3 = int(input("Enter your marks in subject 3 - "))
        mark4 = int(input("Enter your marks in subject 4 - "))
        mark5 = int(input("Enter your marks in subject 5 - "))
    except ValueError :
        print("Only enter numbers!") 
        return

    marks = [mark1,mark2,mark3,mark4,mark5]

    add = sum(marks)
    length = len(marks)
    avg = add / length
    print(f"The average of the entered marks is - {avg}")
    print(f"The highest marks are - {max(marks)}")
    print(f"The lowest are - {min(marks)}")

    marks.sort()
    marks.reverse()

    print(f"The list in the descending order is - {marks}")

manage_marks()

#----------------------------------------------------------------------------------------------------------


# Q4. (OOP + Lists + Exception Handling)

class Student :
    def __init__(self,name,roll_no,marks_list):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = marks_list
    
    
    try :
        def add_mark(self,mark) :
                self.marks_list.append(mark)

    except TypeError :
            print("Only numeric marks are allowed!")


    def get_average(self) :
        add = sum(self.marks_list)
        length = len(self.marks_list)
        avg = add / length
        print(f"The average marks are - {avg}")

    def display_info(self) :
        print("The student info is as followed - ")
        print(f"Name - {self.name}")
        print(f"Roll_No - {self.roll_no}")
        print(f"The marks in the list are as follows - {self.marks_list}")

try :    
    mark1 = int(input("Enter your marks in subject 1 - "))
    mark2 = int(input("Enter your marks in subject 2 - "))
    mark3 = int(input("Enter your marks in subject 3 - "))
except ValueError :
    print("Only enter numbers!") 


marks_list = [mark1,mark2,mark3]
s1 = Student("Pranav",16,marks_list)

s1.add_mark(95)
s1.get_average()
s1.display_info()


#----------------------------------------------------------------------------------------------------------

#Q5. (Dictionaries + Functions + Control Structures)


student_records = {}

def add_student(roll_no, name, year):
    student_records[roll_no] = {
        "name": name,
        "year": year
    }
    print(f"Student {name} added successfully")

def search_student(roll_no):
    student = student_records.get(roll_no)
    if student:
        print(f"Roll No: {roll_no}")
        print(f"Name: {student['name']}")
        print(f"Year: {student['year']}")
    else:
        print("Student not found!")

def display_all():
    if len(student_records) == 0:
        print("No student to display!")
    else:
        for roll_no, details in student_records.items():
            print(f"Roll No: {roll_no} | Name: {details['name']} | Year: {details['year']}")

# Menu
while True:
    print("___ Student Management System ___")
    print("1) Add a student")
    print("2) Search a student")
    print("3) Display all students")
    print("4) Exit")
    
    choice = input("Select waht you want to do -  (1-4): ")
    try :
        if choice == "1":
            roll_no = int(input("Enter roll number: "))
            name = input("Enter name: ")
            year = (input("Enter year of study: "))
            add_student(roll_no, name, year)
        
        elif choice == "2":
            roll_no = int(input("Enter the roll number to search: "))
            search_student(roll_no)
        
        elif choice == "3":
            display_all()
        
        elif choice == "4":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Enter 1-4 only.")
    except ValueError :
        print("Enter correct values!")


#----------------------------------------------------------------------------------------------------------

# Q6. (Sets + Tuples + Modules)
import random
import math
try:
    print("Enter ten unique numbers - ")
    numbers = set()
    for i in range(1,11) :
        num = int(input(f"Enter number - {i}"))
        numbers.add(num)

    numbers = tuple(numbers)

    print(f"Random number 1 - {random.choice(numbers)}")
    print(f"Random number 2 - {random.choice(numbers)}")
    print(f"Random number 3 - {random.choice(numbers)}")

    add = sum(numbers)

    print(f"The square root of the sum of the tuple elements is - {math.sqrt(add):.2f}")


except ValueError:
    print("Enter only numbers!")


#----------------------------------------------------------------------------------------------------------

# Q7. (Lambda + range() + Lists + Exception Handling)

square = lambda x : x ** 2 

squares = list()
for i in range(1,21) :
    square_of_number = square(i)
    squares.append(square_of_number)


print("The square of the even numbers are -")
for i in squares:
    if i % 2 == 0:
        print(i)



#----------------------------------------------------------------------------------------------------------

# Q8. (Tuples + Dictionaries + OOP)

class Employee:
    def __init__(self, emp_id, name, details):
        self.emp_id = emp_id
        self.name = name
        self.details = details    

    def show_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Their name: {self.name}")
        print(f"Their Department: {self.details[0]}")   
        print(f"Their Salary: {self.details[1]}")        


employees = {}

e1 = Employee(1, "Pranav", ("Engineering", 50000))
e2 =Employee(2, "Gauri", ("Marketing", 45000))
e3 =  Employee(3, "Rahul", ("HR", 40000))

employees[1] = e1
employees[2] = e2
employees[3] = e3


for emp_id, emp_object in employees.items():
    print("="*30)
    emp_object.show_details()



#----------------------------------------------------------------------------------------------------------


# Q9. (Strings + Sets + Exception Handling + Modules)

import math

sentence = input("Enter a sentence - ")

sentence = set(sentence) # All unique words will be extracted

sentence = list(sentence)

sentence.sort()

print(f"The unique words in sorted order are - {sentence}")

add = len(sentence)

print(f"The square of the sum of all the unique number is - {math.sqrt(add):.2f}")


#----------------------------------------------------------------------------------------------------------

# Q10. (Mini Project - Comprehensive)
import random
import math
try :
    def basic_aritmetic() :
        print("Welcome to basic calculator!")

        operator = input("Select the task you want to perform (+,-,*,/)")
            
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


    def show_menu():
        print("1) Basic Arithmetic")
        print("2) Scientific Calculations")
        print("3) Generate Random Numbers")
        print("4) Store Result")
        print("5) View History")
        print("6) Exit")

    def scientific_calc() :
        print("Welcome to Scientific calculator!")

        print("Here's what you can do - ")
        print("1)Find the square root of a number!")  
        print("2)Find the ceiling value.")
        print("3)Find the floor value")
        print("4)Find the power of a number")
        print("5)Find the factorial of a number.")
        operator = input("Select the task you want to perform(1-5) -")
            

        if operator == "1" :
            num = int(input("Enter a number to find its square root -"))
            print(f"The square root of {num} is - {math.sqrt(num)}")

        elif operator == "2" :
            num = float(input("Enter a floating number - "))
            print(f"The ceiling value of number {num} is - {math.ceil(num)} ")
        elif operator == "3" :
            num = float(input("Enter a floating number - "))
            print(f"The floor value of number {num} is - {math.floor(num)} ")
        elif operator == "4" :
            base = int(input("Enter the base - "))
            exp = int(input("Enter the exponention - "))
            print(f"The power of the number {base} to {exp} is {math.pow(base,exp)}")
        elif operator == "5" :
            num = int(input("Enter a number to find it's factorial - "))
            print(f"The factorial of the num {num} is - {math.factorial(num)}")
        else :
            print("Enter valid choice!")


    def random_num_gen():
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))
        print(f"Random number: {random.randint(start, end)}")

    def store_result(result):
        if result:
            history[len(history) + 1] = result
            print("Result stored successfully!")
        else:
            print("No valid result to store.")

    def view_history():
        if len(history) == 0:
            print("No calculations yet")
        else:
            for key, value in history.items():
                print(f"Calculation {key}: {value}")
    print("-"*20)
    print("___Welcome to smart calculator and data manager___")
    print("-"*20)

    history = {}  
    while True :
        print("Things you can use - ")
        show_menu()
        choice = input("What do you want to do (1-6) -")

        if choice == "1" :
            basic_aritmetic()
        elif choice == "2" :
            scientific_calc()
        elif choice == "3" :
            random_num_gen()
        elif choice == "4" :
            result = input("Enter the result you want to store - ")  
            store_result(result)
        elif choice == "5" :
            view_history()
        elif choice == "6" :
            print("Exiting...")
            break
        else :
            print("Enter only from choice (1-6).")
except ValueError:
    print("Enter correct values.")