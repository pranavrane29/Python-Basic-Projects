class Mobile :
    def __init__(self,brand,price,ram):
        self.brand = brand
        self.price = price
        self.ram = ram
    
    def display(self):
        print(f"The brand of mobile is - {self.brand}")
        print(f"It's Price is - {self.price}")
        print(f"It's ram is - {self.ram}")
        print("-"*20)
M1 = Mobile("Redmi",14000,16)
M2 = Mobile("Oneplus",52000,16)
M3 = Mobile("Vivo",32000,16)
M4 = Mobile("Ai+",10000,8)


M1.display()
M2.display()
M3.display()
M4.display()


#-----------------------------------------------------------------------------------
            #Task 10
#-----------------------------------------------------------------------------------


#Q1. (Basic Class and Object)

class Car :
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display_info(self) :
        print(f"Brand - {self.brand}")  
        print(f"Model - {self.model}")

C1 = Car("Tata","Nexon")    
C2 = Car("Lamborghini","SVJ")

C1.display_info()
C2.display_info()

#-----------------------------------------------------------------------------------

#Q2. (Using init Constructor)

class Book :
    def __init__(self,title,author,price) :
        self.title = title
        self.author = author
        self.price = price

    def show_details(self) :
        print(f"Title - {self.title}")
        print(f"Author - {self.author}")
        print(f"Price - {self.price}")

B1 = Book("Mahabharata","Gita_Press",200)
B2 = Book("Hogwards","JK_Rowling",449)

B1.show_details()
B2.show_details()


#-----------------------------------------------------------------------------------

#Q3. (Instance Methods and self)

class BankAccount() :

    def __init__(self,account_holder,balance) :
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount) :
        self.balance+= amount
        print(f"Amount Deposited - {amount}")

    def withdraw(self,amount) :
        if self.balance >= amount:
            self.balance -= amount 
            print(f"Amount Withdrawn - {amount}")
        else :
            print("Not enough amount to withdraw!")
    def show_balance(self) :
        print(f"Your current balance is - {self.balance}")


Man1 = BankAccount("Pranav",5001)

Man1.deposit(500)
Man1.show_balance()
Man1.withdraw(1000)
Man1.show_balance()


#-----------------------------------------------------------------------------------

#Q4. (Method with Parameters)

class Students :
    def __init__(self,name,mark) :
        self.name = name
        self.mark = mark


    def calculate_grade(self) :
        if self.mark >= 40 :
            print("Passed!")
        else :
            print("Failed!")

S1 = Students("Pranav",94)
S2 = Students("Tanish",75)
S3 = Students("Kailash",36)


S1.calculate_grade()
S2.calculate_grade()
S3.calculate_grade()


#-----------------------------------------------------------------------------------

#Q5. (Multiple Methods)

class Employee :
    def __init__(self,name,salary) :
        self.name = name
        self.salary = salary

    def display_details(self) :
        print(f"Employee name - {self.name}")
        print(f"Employee's Salary - {self.salary}")

    def give_raise(self,amount) :
        self.salary += amount
        print(f"Your salary increased by - {amount}")

    def yearly_bonus(self) :
        return self.salary * 0.10
    
emp = Employee("Pranav",70000)
emp.display_details()
emp.give_raise(5000)
y_bonus = emp.yearly_bonus()
print(f"Employees Yearly bonus is - {y_bonus}")


#-----------------------------------------------------------------------------------

# Q6. (Real-world Object Modeling)

class MobilePhone :
    def __init__(self,brand,model,battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage

    def charge(self,percent) :
        if self.battery_percentage == 100 :
            print("Battery charged to 100%,Pls do not overcharge.")
        else :
            self.battery_percentage += percent

    def use_phone(self,minutes) :
        for i in range(minutes):
            if i % 10 == 0 :
                self.battery_percentage -= 1
            else : 
                pass

    def show_status(self) :
        print(f"Mobile Brand - {self.brand}")
        print(f"Mobile Model - {self.model}")
        print(f"Current battery percentage - {self.battery_percentage}")

Phone = MobilePhone("Oneplus","Nord_CE_3",100)

Phone.use_phone(120)
Phone.charge(5)
Phone.show_status()


#-----------------------------------------------------------------------------------

#Q7. (Combining Concepts)

class Rectangle :
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self) :
        v_area = self.length * self.width
        return v_area

    def perimeter(self) : 
        v_perimeter = 2 * (self.length + self.width)
        return v_perimeter
    
    def display(self) :
        print(f"Length of the rectangle is - {self.length} cm")
        print(f"Width of the rectangle is - {self.width} cm")
        print(f"The area of the rectangle is - {self.area()}")
        print(f"The perimeter of the rectangle is - {self.perimeter()}")



length = int(input("Enter a length (in cm) - "))
width = int(input("Enter a width (in cm)- "))


Rect = Rectangle(length,width) 

Rect.area()
Rect.perimeter()
Rect.display()


#-----------------------------------------------------------------------------------

#Q8. (Updating Attributes)

class Player :
    def __init__(self,name,score,level) :
        self.name = name
        self.score = score
        self.level = level

    def increase_score(self,points) :
        self.score += points

    def level_up(self) :
        self.level += 1

    def show_progress(self) :
        print("_____Current Stats of the player_____ ")
        print(f"Name of the player - {self.name}")
        print(f"Score - {self.score}")
        print(f"Level - {self.level}")

Player1 = Player("Pranav",30,18)
Player2 = Player("Virat",112,95)


Player1.show_progress()
Player2.show_progress()

print("="*50)

Player1.increase_score(152)
Player2.increase_score(195)
Player1.level_up()
Player2.level_up()
Player1.level_up()
Player2.level_up()
Player1.level_up()
Player2.level_up()


print("After 3 matches the stats of this both players went up!")

Player1.show_progress()
Player2.show_progress()


#-----------------------------------------------------------------------------------


#Q9. (Debugging OOP Code)

''' __________Incorrect code___________'''

class Person:
    def __init__(name, age): #missing self as parameter
        name = name #Missing self.name 
        age = age #Missing self.age
    
    def introduce(): #missing self as parameter
        print("My name is" name "and I am" age "years old.") 
        '''print statment must seperate variables with (,) to avoid error 
        or use f-string(best-way).Also variable must be called with self keyword'''

p1 = Person("Rahul", 25)
p1.introduce()

''' __________Corrected code___________'''

class Person:
    def __init__(self,name, age): 
        self.name = name 
        self.age = age 
    
    def introduce(self): 
        print(f"My name is {self.name} and I am {self.age} years old.") 

p1 = Person("Rahul", 25)
p1.introduce()

#-----------------------------------------------------------------------------------


#Q10. (Mini Project - Combined OOP)


'''______Simple Library Management System_______'''

class Book :
    def __init__(self,title,author,status="Available"):
        self.title = title
        self.author = author
        self.status = status

    def issue_book(self) :
        if self.status == "Issued" :
            print("Book not available to be issued!")
        else :
            self.status = "Issued"
            print("The book was issued successfully!")
    
    def return_book(self) :
        if self.status == "Available" :
            print("The book was not issued!")
        else :
            self.status == "Available"
            print("The book was returned successfully!")

    def show_info(self) :
        print(f"Book Details - ")
        print(f"Title - {self.title}")
        print(f"Author - {self.author}")
        print(f"Status - {self.status}")
        print("="*30)


B1 = Book("Mahabharata","Ved Vyas","Available")
B2 = Book("Maths for 10th","Nirali_Publication","Issued")
B3 = Book("English Literature","Rusking Bond")
B4 = Book("Oxford Dictionary","Oxford_Institute","Issued")

library = {
    "b1": B1,
    "b2" : B2,
    "b3" : B3,
    "b4" : B4
}


while True :
    print("____WELCOME TO LIBRARY MANGAEMENT SYSTEM____")
    print("Here are some things you can do ---> ")
    print("1)Add a new book")
    print("2)Issue a new book")
    print("3)Return a new book")
    print("4)Show all books")
    print("5)Exit")

    choice = input("What do you want to do (1-5) - ")

    if choice == "1" :
       book_id = input("Enter unique identity for the book (ex-A1,K7,etc) - ")
       title = input("Enter the title of the book - ")
       author = input("Enter author's name - ")
       library[book_id] = Book(title, author, "Available")
       print("Book added successfully!")


    elif choice == "2" :
        issue = input("Enter unique identity of the book you want to issue - ")
        if issue in library :
            library[issue].issue_book()
        else:
            print("Book not found!")

    elif choice == "3" :
        b_return = input("Enter unique identity of the book you want to return - ")
        if b_return in library:
           library[b_return].return_book()
        else:
           print("Book not found!")

    elif choice == "4" :
        print("All available books in library are - ")
        for key in library.values() :
            key.show_info()
    elif choice == "5" :
        print("Exiting...")
        break 
    else :
        print("Enter valid choice (1-5) - ")


