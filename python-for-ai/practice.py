students = {}

while True:
    print("Welcome to Student Managment System.")
    
    print("1 - Add a student")
    print("2 - Update a students marks ")
    print("3 - Search a student by roll")
    print("4 - Display all students")
    print("5 - Remove a specific student")
    print("6 - Exit")
    choice = input("Select What you want to do - ")

    if choice == "1" :
        roll = int(input("Enter your rollno - "))
        name = input("Enter your name -")
        age = int(input("Enter your age -"))
        marks = int(input("Enter your marks - "))
        students[roll] = {"name" : name , "age" : age , "marks" : marks}
        print("Student added successfully!")

    elif choice == "2" :
        roll = int(input("Enter roll no to update their marks - "))
        if roll in students :
            new_marks = int(input("Enter marks to be updated"))
            students[roll]["marks"] = new_marks
            print("Marks updated")
        else :
            print("Roll no doesn't exist")

    elif choice == "3" :
       roll = int(input("Enter the roll no to search - "))
       if roll in students :
           print(f"Details - {students[roll]}")
       else :
           print("The student doesn't exist!")

    elif choice == "4" :
        if students :
           for key, value in students.items():
            print(f"Roll = {key}, Name = {value['name']}, Age = {value['age']}, Marks = {value['marks']}")
        else :
            print("No students enrolled yet")
    elif choice == "5" :
        roll = int(input("Enter a roll no to remove them - "))
        if roll in students :
            students.pop(roll)
            print("Student removed!")
        else :
            print("Such student doesn't exist")
    elif choice == "6" :
        print("Exiting...")
        break
    else :
        print("Enter only valid choice - (1 to 6)")

stu = {
    name : "Pranav",
    age : 18

}


student = {
    "roll_no" : {
        "name" : "Pranav",
        "age" : 18
    }
}

removed = student.pop["name"]
print(removed)


d = dict()
d.setdefault("name" , 0)