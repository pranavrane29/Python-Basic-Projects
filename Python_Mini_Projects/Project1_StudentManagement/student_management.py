#----------------------------------------------------------------------------------
'''
Project 1 - Student Management System
Made by Pranav Rane
'''
#----------------------------------------------------------------------------------

'''Functions Definitions followed by actual 
system.
'''

def add_student() : # Adds Students data 
    try :
        roll_no = int(input("Enter the roll_no - "))
        if roll_no in student_records :
            print("Rollno already exists!")
        else :
            
            name = input("Enter your name - ")
            if name.isdigit():
                print("Name can only be in string!")
            else :
                mark1 = int(input("Enter your marks in Science - "))
                mark2 = int(input("Enter your marks in Social Science - "))
                mark3 = int(input("Enter your marks in Maths - "))
                mark4 = int(input("Enter your marks in Hindi/Sanskrit - "))
                mark5 = int(input("Enter your marks in English - "))
               
                if (mark1 > 100 or mark2 > 100 or mark3 > 100 or mark4 > 100 or mark5 > 100) or \
                (mark1 < 0 or mark2 < 0 or mark3 < 0 or mark4 < 0 or mark5 < 0):
                    print("Marks must be between 0 and 100!")
                else:
                    total = (mark1 + mark2 + mark3 + mark4 + mark5)

                    percentage, grade = calculate_grade(total)
                
                    student_records[roll_no] = {
                    "name" : name,
                    "Science_Marks" : mark1,
                    "Social_Science_Marks" : mark2,
                    "Maths_Marks" : mark3,
                    "H/S_Marks" : mark4,
                    "English_Marks" : mark5,
                    "percentage" : percentage,
                    "grade" : grade
                    }
    except ValueError :
        print("Enter correct Value!")    

def view_all() : # Used to view all the students details if any.
    if not student_records :
        print("Data doesn't exist")
    else :
        fmt = "{:<8} {:<15} {:<8} {:<8} {:<8} {:<8} {:<8} {:<12} {:<6}"
        print("=" * 105)
        print(fmt.format("Roll No", "Name", "Sci", "SocSci", "Math", "Hin/San", "Eng", "Percentage", "Grade"))
        print("=" * 105)
        
        for roll_no,details in student_records.items() :
            print(fmt.format(
                roll_no,
                details["name"],
                details["Science_Marks"],
                details["Social_Science_Marks"], 
                details["Maths_Marks"],
                details["H/S_Marks"],
                details["English_Marks"],
                f"{details['percentage']:.2f}%", # rounds percentage upto 2 decimal places
                details["grade"]
            ))
        print("=" * 105)

   
def search_student() : # Searchs student a student by their roll_no
    try :
        if not student_records :
            print("Data doesn't exist")
        else :
            roll_no = int(input("Enter a rollno to view its data - "))
            if roll_no in student_records :
                details = student_records[roll_no]
                print("\n" + "=" * 40)
                print(f"       FOUND RECORD (Roll No: {roll_no})")
                print("=" * 40)
                print(f" Name:        {details['name']}")
                print(f" Science:     {details['Science_Marks']}")
                print(f" Social Sci:  {details['Social_Science_Marks']}")
                print(f" Maths:       {details['Maths_Marks']}")
                print(f" Hindi/Sans:  {details['H/S_Marks']}")
                print(f" English:     {details['English_Marks']}")
                print("-" * 40)
                print(f" Percentage:  {details['percentage']:.2f}%")
                print(f" Grade:       {details['grade']}")
                print("=" * 40)
            else :
                print("Record not found for this key!")
    except :
        print("Pls enter correct values!")


def delete_student()  : # Removes a students data
    try :
        roll_no = int(input("Enter the roll no whose data you want to remove - "))
        if roll_no in student_records :
            print(f"Removing roll_no {roll_no}'s data.")
            del student_records[roll_no]
            print("Data Removed!")
        else :
            print("Roll no does not exists")
    except ValueError :
        print("Pls enter correct value!")


def calculate_grade(total)  : # calculates grade and send back to add add_student()
    percentage = (total / 500) * 100
    grade = ""
    if percentage >= 90 :
        grade = "A"
    elif percentage >= 80 :
        grade = "B"
    elif percentage >= 70 :
        grade = "C"
    elif percentage >= 60 :
        grade = "D"
    elif percentage >= 50 :
        grade = "E"
    else :
        grade = "F"
    return percentage,grade

def update_student()   : #updates any required values of student
    try :
        roll_no = int(input("Enter a rollno to change its data - "))
        if roll_no in student_records :
                
            print("What do you want to change - ")
            print("1)Name")
            print("2)Marks of Science")
            print("3)Marks of Math")
            print("4)Marks of Social Science")
            print("5)Marks of Hindi/Sanskrit")
            print("6)Marks of English ")

            choice = input("Enter your choice (1 - 6) -")
            if choice == "1" :
                name = input("Change the name to - ")
                if name.isdigit():
                    print("Name can only be in string!")
                else :
                    student_records[roll_no]['name'] = name
                    print("Name updated")
            elif choice == "2" :
                mark1 = int(input("Enter updated marks - "))
                student_records[roll_no]['Science_Marks'] = mark1
                print("Marks Updated!")
            elif choice == "3" :
                mark1 = int(input("Enter updated marks - "))
                student_records[roll_no]['Maths_Marks'] = mark1
                print("Marks Updated!")
            elif choice == "4" :
                mark1 = int(input("Enter updated marks - "))
                student_records[roll_no]['Social_Science_Marks'] = mark1
                print("Marks Updated!")
            elif choice == "5" :
                mark1 = int(input("Enter updated marks - "))
                student_records[roll_no]['H/S_Marks'] = mark1
                print("Marks Updated!")
            elif choice == "6" :
                mark1 = int(input("Enter updated marks - "))
                student_records[roll_no]['English_Marks'] = mark1
                print("Marks Updated!")
            else :
                print("Pls Enter the correct value(1-6)")
            total = student_records[roll_no]['Science_Marks'] + student_records[roll_no]['Social_Science_Marks'] + student_records[roll_no]['Maths_Marks'] + student_records[roll_no]['English_Marks']  + student_records[roll_no]['H/S_Marks']
            percentage, grade = calculate_grade(total)
            student_records[roll_no]['percentage'] = percentage
            student_records[roll_no]['grade'] = grade
        else :
             print("The rollno doesnt exist!")
    except ValueError :
        print("Pls enter correct values!")

def class_report(): # Bonus Task 
    if not student_records:
        print("No data to generate report!")
        return
    else:
        #Calculating topper
        highest = -1.0
        name = ""

        for key,value in student_records.items() :
            pct = value['percentage']

            if pct > highest :
                highest = pct
                name = value['name']
        print("*"*10)
        print(f"{name} achieved highest percentage - {highest}")
        print("*"*10)


        #Finding Average Percentage
        all_students = len(student_records)
        total_percentage = 0 
        for key,value in student_records.items():
            total_percentage += value['percentage']
        avg_percentage = total_percentage / all_students
        print(f"Average Percentage are - {avg_percentage}")
        print("*"*10)


        #Pass/Fail 
        passed = 0
        failed = 0
        for key,value in student_records.items():
            if value['percentage'] < 50 :
                failed += 1
            else :
                passed += 1
        print(f"Total student passed are - {passed}")
        print(f"Total Student Failed are - {failed}")

    

def show_menu() : #Shows what you can perform
    print("What you can perfrom - ")
    print("1)Add a Student")
    print("2)View All Students")
    print("3)Search a student by their Roll Number")
    print("4)Update a student record")
    print("5)Remove a student data")
    print("6)See Class Report")
    print("7)Exit")
     


'''Actual System Below'''


student_records = {} #(Global Declaration) Holds students details

def main() :
    while True :
        try :
            print("-" * 58)
            print("_____-Welcome to Student Management System!_____")
            print("Note - Asks for user input to perform a specific action.")
            print("-" * 58)

            show_menu()

            choice = input("Enter what you want to do (1 - 7) - ")
            print("-" * 30)
            if choice == "1" :
                add_student()
            elif choice == "2" :
                view_all()
            elif choice == "3" :
                search_student()
            elif choice == "4" :
                update_student()
            elif choice == "5" :
                delete_student()
            elif choice == "6" :
                class_report()
            elif choice == "7" :
                print("Exited Successfully!")
                break
            else :
                print("Pls enter a valid choice(1 - 7)")
        except ValueError :
            print("Enter correct value!")

if __name__ == "__main__":
    main()
