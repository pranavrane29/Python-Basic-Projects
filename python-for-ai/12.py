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
            year = int(input("Enter year of study: "))
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


