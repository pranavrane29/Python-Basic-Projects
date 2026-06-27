a = 1,2,3,4,5,6,7,8,9,10

b = tuple("hello")
print(b)

print(type(a))


c = ((12,3) , [12,3] , "Hello" , 1, 2, 3)

print(c)

print(c.count(12))
print(c.index("Hello"))


#----------------------------------------------------------------------------------

                #Task 7

#----------------------------------------------------------------------------------

#Q1. (Creating Tuples)

a = (1,2,3,4,5) #Tuple using paranthesis

b = (10,"Hello",19.11,False) #Tuple of mixed datatypes

c = () #First way to make an empty tuple
c = tuple() #Second way to make an empty tuple 

d = (99,) # A Tuple with single value

print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))

print(d)
print(type(d))

'''To store a single element in a tuple you must store it in paranthisis 
and seperate it by comma(,) beacuse if you just wrote the integer as it is 
in the paranthesis, python thinks that it is a single value assigned to the 
variable on which operations are need to be performed.'''

#----------------------------------------------------------------------------------

#Q2. (Tuple Packing)

a = "Pranav", 18, "Malkapur"
print(a)
print(type(a))

name,age,city = a 
print(name)
print(age)
print(city)

#----------------------------------------------------------------------------------

#Q3. (Indexing and Negative Indexing)

colors = ('red', 'green', 'blue', 'yellow', 'purple', 'orange')
print(colors)

print(colors[0]) #First element
print(colors[2]) #Third element
print(colors[-1]) #Last element
print(colors[-2]) #Second last element

index = int(input("Enter an index to print the element at that index - "))
if index < 5 or index < -6 :
    print(f"The element at {index} index is - {colors[index]}")
else :
    print("Pls enter valid index!")

#----------------------------------------------------------------------------------

#Q4. (Slicing Tuples)

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"Original tuple is - {numbers}")

print(f"The elements from index 2 to 7 are - {numbers[2:7]}") 

print(f"The first five elements are - {numbers[0:5]}")

print(f"The last 4 elements are - {numbers[-1:-5:-1]}")

print(f"Every second element are - {numbers[0::2]}")

print(f"The entire tuple in reverese becomes - {numbers[-1::-1]}")

'''slice[start,stop,step]--> i)start indicates the starting position of a element 
ii)stop indicates the stopping point of the range(exclusive)
iii)step indicates the elements it will skip and print '''


#----------------------------------------------------------------------------------

#Q5. (Nested Tuples)

matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(f"The original tuple - {matrix}")

print(f"The first row is - {matrix[0]}")
print(f"The element at second row, third column is - {matrix[1][2]}")
print(f"The element at third row, first column is - {matrix[2][0]}")

#----------------------------------------------------------------------------------

#Q6. (Iterating and Unpacking)

student = ('Rahul', 20, 'Computer Science', 'A')

i = 1
for value in student :
    print(f"Value {i} - {value}")
    i+=1

name,age,branch,grade = student

print(f"My name is - {name}")
print(f"I am {age} years old!")
print(f"I am a {branch} department student")
print(f"I have scored {grade} in my last semester")


#----------------------------------------------------------------------------------

#Q7. (count() Method)

grades = ('A', 'B', 'A', 'C', 'A', 'B', 'D', 'A', 'B')
print(f"The grades are - {grades}")

print(f"The grade 'A' have appeared {grades.count('A')} times")
print(f"The grade 'B' have appeared {grades.count('B')} times")

score = input("Enter a grade to check how many times it is stored in the tuple - ")

print(f"The grade - '{score}' have apperaed {grades.count(score)} times")

#----------------------------------------------------------------------------------

#Q8. (index() Method)

fruits = ('apple', 'banana', 'cherry', 'banana', 'mango', 'apple')
print(f"The original fruits tuple - {fruits}")

print(f"The 'banana' firstly appeared at index - {fruits.index('banana')}")
print(f"The 'banana' firstly appeared from index 2 at index - {fruits.index('banana',2)}")

try :
    print(f"The fruit 'kiwi' is found at index - {fruits.index('kiwi')}")
except :
    print("The fruit 'kiwi' is not in the tuple!")
finally :
    print("Q8 completed!")

#----------------------------------------------------------------------------------

#Q9. (Immutability of Tuples)

coordinates = (10, 20)

try : 
    coordinates[0] = 11
    coordinates.append(8) #append() doenst work for tuples

except : 
    print("We cannot change an element in tuple(Immutable)")
    print("Also we cannot append an element in our tuple")
finally :
    l_coordinates = list(coordinates)

    l_coordinates[0] = 11
    l_coordinates.append(30) 

    coordinates = tuple(l_coordinates)

    print(f"After making changes into our tuple using list, we have - {coordinates}")

'''Errors - i)TypeError: 'tuple' object does not support item assignment
ii) AttributeError: 'tuple' object has no attribute 'append'
This errors happens when we try to change or append a value in a tuple.We cannot do that. 
we first need to convert a tuple into a list to make changes and then return it back to it's
original form i.e Tuple'''


#----------------------------------------------------------------------------------

#Q10. (Mini Project - Combined Concepts)

#  Student Record Program

name = input("Enter your name - ")
roll_no = int(input("Enter your roll number - "))

marks1 = int(input("Enter your marks in first subject - "))
marks2 = int(input("Enter your marks in second subject - "))
marks3 = int(input("Enter your marks in third subject - "))

info = name,roll_no,marks1,marks2,marks3 # Packing into a tuple

print(f"Your complete information is - {info}")

u_name,u_rollno,u_marks1,u_marks2,u_marks3 = info #Unpacking from the tuple 

print(f"Your name is - {u_name}")
print(f"Your rollno is - {u_rollno}")

print(f"Your marks in subject 1 is - {u_marks1}")
print(f"Your marks marks in subject 2 is - {u_marks2}")
print(f"Your marks marks in subject 3 is - {u_marks3}")

print(f"Checking how many times 95 appeared (if any) - {info.count(95)}")

multi_students = (("Pranav",18,"2nd Year"), ("Gauri",19,"3rd Year") , ("David",16,"1st Year")) #Another tuple holding nested tuple

print(f"First student info is - {multi_students[0]}")
print(f"Second student info is - {multi_students[1]}")
print(f"Third student info is - {multi_students[2]}")


#--------------------------------------------------------------------------------------------------------------------------------------------------




    