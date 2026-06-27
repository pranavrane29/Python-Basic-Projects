st = {"1",2,3,4,5,6,1,"8",9,10}
print(st)

print(type(st))

st1 = {"Pranav",2,2.5,True}
st1.add(3)
print(st1)


#----------------------------------------------------------------------------------------

#Q1. (Creating Sets)

st1 = {1,2,3,4,5} #A set with 5 integers.
print(st1)
print(type(st1))

st2 = {2,True,2.5,"Hola"} #A set of mixed datatypes
print(st2)
print(type(st2))

st3 = set() #empty set
print(st3)
print(type(st3))

st4 = set("hello") #using string constructor to print hello
print(st4)
print(type(st4))

'''Set only stores the unique values, so if someone tried to store 
a duplicat evalue in a set, it automatically get removed'''


#----------------------------------------------------------------------------------------

#Q2. (Characteristics of Sets)

numbers = {10, 20, 30, 20, 40, 10, 50}

print(f"OG Set - {numbers}")
'''The duplicate values in the set are removed automatically'''

'''The sets are unordered, i.e they are not stored with indexing but it 
doesn't mean that they will be displayed randomly. However different devices may display
random outputs'''

try:
    print(numbers[0]) #Will show TypeError as set is not indexed
except :
    print("Sets are unordered and can't be indexed.")


#----------------------------------------------------------------------------------------

#Q3. (Membership Testing)

colours = set()

for i in range(1,6):
    colour = input(f"Enter the {i} colour - ")
    colours.add(colour)

print(f"Five colours are - {colours}")

check = input("Enter the colour you want to check if it exists in the set - ")

if check in colours  :
    print(f"The colour {check} exists in our set!")
if check not in colours :
    print(f"The colour {check} doesn't exist in our set!")

#----------------------------------------------------------------------------------------

#Q4. (add(), remove(), discard())

fruits = {'apple', 'banana', 'mango'}

print(f"The set is - {fruits}")

fruits.add("orange") 
print(f"After adding orange to our set, the set becomes - {fruits} ")

fruits.add("banana") #Doesn't allow duplicates

fruits.remove("mango")
print(f"After removing mango from our set, the set becomes - {fruits} ")

fruits.discard("grape")
print(f"After discarding grape from our set, the set ramains the same - {fruits} ")
'''.discard doesn't give error if the element is not present in our set, unlike remove()'''


#----------------------------------------------------------------------------------------

#Q5. (pop() and clear())

s = {100, 200, 300, 400, 500}

print(f"OG set - {s}")

s.pop()
print(f"After popping a random element, our set is - {s}")

s.clear()
print(f"After clearing an entire set, we have nothing - {s}")

#----------------------------------------------------------------------------------------

#Q6. (update() and copy())

set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}

print(f"Set1 - {set1}")
print(f"Set2 - {set2}")

set3 = set1.copy()
print(f"The copy of set1 is - {set3}")

set1.update(set2)
print(f"After updating set1 with elements of set2, set1 becomes - {set1}")

#----------------------------------------------------------------------------------------

#Q7. (Union and Intersection)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f"A set - {A}")
print(f"B set - {B}")

print(f"A uniting with B becomes - {A.union(B)} ")
print(f"A intersection with B gives - {A.intersection(B)}")

'''You can also use "|" to make set union and also & to intersect two sets.'''

'''i)union - Gives common elements from two sets, except unique ones
ii)intersection - Gives unique elements from two sets, except common ones '''

#----------------------------------------------------------------------------------------

#Q8. (Combined Methods)

numbers = set()

print("Enter any 6 numbers - (dont add 90 & 91)")
for i in range(1,7):
    number = int(input(f"Enter number {i} - "))
    numbers.add(number)

print(f"The set becomes - {numbers}")

numbers.add(90)
numbers.add(91)

print(f"After adding 90 & 91, our set becomes - {numbers}")

numbers.discard(90)
print(f"After removing 90 we have -{numbers}")

print(f"Therefore the final set remains - {numbers}")
print(f"The length of our final set is - {len(numbers)}")

#----------------------------------------------------------------------------------------

#Q9. (Practical Application)

scores = [85, 92, 78, 92, 85, 88, 95, 78]
print(f"OG list - {scores}")

score = set(scores) #list converted to set
print(f"After conversion of the list to set - {score}") #Prints unique scores


scores = list(score)
scores.sort()
print(f"After sorting the list - {scores}")

print(f"The total number of unique scores are - {len(score)}")


#----------------------------------------------------------------------------------------

#Q10. (Mini Project - Combined Concepts)

#Unique Item Collector

items = {1,2,3,4,5,6,7,8}
while True :
    print("-" * 30)
    print("Welcome to Unique item collector!")
    print("List of things you can do")
    print("1 - adding an item")
    print("2 - removing an item(discarding)")
    print("3 - show all unique item")
    print("4 - checking item existance")
    print("5 - clear all items")
    print("6 - Exit Menu")

    choice = (input("Enter what you want to do as number -"))

    if choice == "1":
        add = input("Enter what you want to add - ")
        items.add(add)
        print(f"Item {add} added succesfully to our set!")

    elif choice == "2" :
        remove = input("What do you want to remove - ")
        items.discard(remove)
        print(f"Item {remove} successfully removed from the set!")

    elif choice == "3" :
        print(f"All unique items are - {items}")

    elif choice == "4" :
        check = input("Enter what do you want to check -")
        if check in items :
            print("The entered item exists in the set.")
        else :
            print("The entered item doesn't exist in our set.")

    elif choice == "5" :
        items.clear()
        print("Set cleared. It is now empty.")

    elif choice == "6" :
        print("Exiting...") 
        break  

    else :
        print("Enter a valid number.")
