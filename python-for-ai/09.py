farmer = {
    "name" : "Pranav",
    "crop" : "Wheat",
    "land_size" : 4 #in acres
}

print(farmer["crop"])

farmer["irrigation_type"] = "drip"

for key,value in farmer.items() :
    print(key, ':' , value)

fruits = dict((("name1", "mango"),("name2" , "Apple")))
print(fruits)

# You have this list of pairs from a sensor reading two crop fields:
data = [("field1", "Wheat"), ("field2", "Rice")]

# Convert it into a dictionary using dict()
# Then print the crop for field2
# Then try creating the SAME dictionary using {} syntax instead, manually

data_d = dict(data)
print(data_d["field2"])
data_d1 = {
    "field1" : "Wheat",
    "field2" : "Rice"
}

data_d.pop("field1")

del farmer

l = [1,2,3,4,5]
print(l)
del l 
print(l)

farmer = {
    "name": "Pranav",
    "crop_details": {
        "crop": "Wheat",
        "land_size": 4
    }
}

print(farmer["crop_details"]["crop"]) 

print(farmer.get("name"))
print(farmer.keys())
print(farmer.values())
print(farmer.items())



field = {"crop": "Wheat", "yield_tons": 12}

# 1. Use setdefault to add "irrigation" with default "manual" — print the result
# 2. Use update() to change yield_tons to 15 AND add a new key "season": "Rabi"
# 3. Make a real copy of field called field_backup
# 4. In field_backup, change crop to "Mustard"
# 5. Print both field and field_backup to prove they're independent

#--------------------------------------------------------------------------------------------------------------------------------------

            #Task 9 

#--------------------------------------------------------------------------------------------------------------------------------------


# Q1. (Creating Dictionaries)

d1 = {} #empty dictionary method 1 
print(d1)
print(type(d1))

d2 = dict() #empty dictionary method 2
print(d2)
print(type(d2))

#A dictionary with string keys (name, city, course).
d3 = {
    "name" : "Pranav",
    "city" : "Malkapur",
    "course" : "Ai/ML"
}
print(d3)
print(type(d3))


#A dictionary with integer keys.
d4 = {
    1 : "Pranav",
    2 : "Gauri",
    3 : "Ishant"
}
print(d4)
print(type(d4))


#A mixed data type dictionary (string, int, float).
d5 = {
    "name" : "Pranav",
    "age" : 18,
    "percentage" : 88.47,
    "is_verified" : True
}
print(d5)
print(type(d5))

'''Dictionaries are data structures are made with either {} or dict().
It stores the data in key value pair assigned using colon(:).
Such as "name" : "Pranav"'''


#--------------------------------------------------------------------------------------------------------------------------------------

# Q2. (Accessing and Modifying Elements)

student = {
"name": "Pranav",
"age": 18,
"city": "Malkapur",
"marks": 88.47
}
print(f"The OG dictionary - {student}")
print(f"The value at 'name' is - {student['name']} ")

student["marks"] = 92.00

student["grade"] = "A"

print(f"Updated Dictionary - {student}")


#--------------------------------------------------------------------------------------------------------------------------------------

#Q3. (get(), keys(), values(), items())

person = {
    "name": "Priya",
    "age": 21,
    "profession": "Engineer"
        }

print("Dictionary - ", person)
print(f"The value at 'age' and 'salary'(doesn't exists) with .get() is - {person.get('age')} and {person.get('salary')} respectively")

print(f"All keys in our person dictionary are - {person.keys()}")

print(f"All values in our dictionary are - {person.values()}")

print(f"All key-value pairs are - {person.items()}")

#--------------------------------------------------------------------------------------------------------------------------------------

#Q4. (Nested Dictionary)

students = {
"s1": {
    "name": "Rahul", "age": 20, "marks": 88
    },

"s2": {
    "name": "Sneha", "age": 21, "marks": 95
    }
}

print("Dictionary - ", students)

print(f"First student details are - {students['s1']}")
print(f"Second student details are - {students['s2']}")

students["s1"]["math_marks"] = 90
print(f"The updated dictionary is - {students}")

#--------------------------------------------------------------------------------------------------------------------------------------

#Q5. (update() and pop())

info = {
    "brand": "Samsung",
    "model": "A52",
    "price": 25000
    }
print(f"The dictionary - {info}")

info["color"] = "Black"
info["price"] = 24000
print(f"The color and price key was updated!")

removed = info.pop("model")

print(f"The removed value is - {removed}")

print(f"The final dictionary - {info}")

#--------------------------------------------------------------------------------------------------------------------------------------

#Q6. (popitem() and clear())

person = {
    "name" : "Pranav Paul",
    "age" : 18,
    "spouse" : "Unmarried(RC) :<",
    "place" : "Sambhajinagar",
    "marks" : 76
}

last_item = person.popitem()
print(f"First Removed item - {last_item}")
last_item = person.popitem()
print(f"Second Removed item - {last_item}")

print(f"Final dictionary after - {person}")

person.clear()

print("Dictionary cleared!")

#--------------------------------------------------------------------------------------------------------------------------------------

#Q7. (copy() and setdefault())

d = {"a": 1, "b": 2}

d1 = d.copy()

d1.setdefault("c", 3) # adds, cause it ain't there
d1.setdefault("a","Unknown") # returns the value of a cause its present 

print(f"The original dictionary - {d}")
print(f"The copied dictionary - {d1}")

#--------------------------------------------------------------------------------------------------------------------------------------

#Q8. (fromkeys() and Membership)

l = ["name", "age", "city"]

di = dict.fromkeys(l) # creates a dictionary with all keys value set to null

print(f"Original values - {di}")

n = input("Enter your name - ")
a = int(input("Enter your age - "))
c = input("Enter your city name - ")

di["name"] = n
di["age"] = a
di["city"] = c

print(f"Your details are - {di}")

check = input("Enter a key to check if exists - ")

if check in di :
    print(f"The key {check} exists in our dictionary")
else : 
    print(f"The key {check} doesn't exists in our dictionary")

#--------------------------------------------------------------------------------------------------------------------------------------

# Q9. (Practical Application)

n = input("Enter your name - ")
p = int(input("Enter your phone number - "))
e = input("Enter your email - ")


contact_info = {
    "name" : n,
    "phone_number" : p,
    "email" : e
}

check = input("Do you want to check the contact info? (y/n) - ")
if check == "y" :
    print(f"Name - {contact_info.get('name')}")
    print(f"Phone_Number - {contact_info.get('phone_number')}")
    print(f"Contact - {contact_info.get('email')}")
else :
    print("Bye")

#--------------------------------------------------------------------------------------------------------------------------------------

#Q10. (Mini Project - Combined Concepts)

#Student Management System

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