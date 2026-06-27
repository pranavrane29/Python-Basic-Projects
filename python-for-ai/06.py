''''fruits = ["Apple", "Banana", "Orange", "Kiwi"]

print(fruits)

for fruit in fruits :
    print(fruit)

print(fruits[-1::-1])

a = [1,5,2,3,4,5,6,7,8,9,10]
print((a))

b = [1,1.2,True,"Bob"]
print(b)

a.append(11)
a.index(5)
a.insert(2,2.5)
a.clear()
b = a.copy()
a.pop(6)
a.remove(5)
a.count(5)
a.extend(b)
a.sort()
a.reverse()'''

#---------------------------------------------------------------------------------

                    #Task 6

#---------------------------------------------------------------------------------


#Q1. (Creating Lists) 

a = [1,2,3,4,5] #direct list of 5 integers
print(a)

empty = [list()] #empty list with [] & ()
print(empty)

mix = [1,2.5,True,"Hello"] #list with mixed datatypes
print(mix)

zeroes_7 = [0] * 7 #list with 7 zeroes stored in it 
print(zeroes_7)

'''So, basically we create the list with the [] and list()
with [] you just type in the data and the python is smart enough to understand 
that this is a list, secondly using list() to make a list is just another way to make list
Basically, list() takes the argument as iterable format and makes a new list out of each element 
whereas, [] just takes the argument and makes a list and stores the argument as standalone element.'''

#---------------------------------------------------------------------------------

#Q2. (Indexing and Negative Indexing) 

fruits = ["apple", "banana", "mango", "orange", "grape"]

print(f"First item - {fruits[0]}") #first item
print(f"Third item - {fruits[2]}") #third item
print(f"Last item - {fruits[-1]}") #last item
print(f"Second last item - {fruits[-2]}") #second last item

item = int(input("Enter from 0 to 4 or -1 to -5 to check the element stored at that index -"))
print(f"The element present at index {item} is = {fruits[item]}")

#---------------------------------------------------------------------------------

#Q3. (Slicing Lists) 

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] 

print(f"First 4 elements are - {numbers[0:4]}")
print(f"Last 3 elements are - {numbers[7:]}")
print(f"Elements from index 2 to 7 are - {numbers[2:7]}")
print(f"Every second element is - {numbers[0::2]}")
print(f"The entire list in reveresed order is - {numbers[-1::-1]}")

'''slice[start,stop,step]--> i)start indicates the starting position of a element 
ii)stop indicates the stopping point of the range(exclusive)
iii)step indicates the elements it will skip and print '''

#---------------------------------------------------------------------------------

#Q4. (Modifying Lists) 

colors = ["red", "blue", "green", "yellow"] 
print(f"Original list - {colors}")

colors[1] = "purple"
print(f"List after changing blue to purple is - {colors}")

colors[-1] = "black"
print(f"List after changing last item to black is - {colors}")

#---------------------------------------------------------------------------------

#Q5. (append() and insert()) 

cities = [] #empty list

city1 = input("Enter a city name - ")
city2 = input("Enter a city name - ")
city3 = input("Enter a city name - ")
city4 = input("Enter a city name - ")
city5 = input("Enter a city name - ")

cities.append(city1)
cities.append(city2)
cities.append(city3)
cities.append(city4)
cities.append(city5)


cities.insert(1,"Nurburg")

print(cities)

#---------------------------------------------------------------------------------

#Q6. (remove(), pop(), and clear()) 

items = [10, 20, 30, 20, 40, 50] 
print(f"Original list - {items}")

items.remove(20)
print(f"List after first 20 is removed - {items}")

item_3 = items[3]
items.pop(3)
print(f"List after removing item {item_3} at index 3 becomes - {items}")

items.pop()
print(f"List after removing last item becomes - {items}")

items.clear
print(f"Clearing the entire list - {items}")

'''remove() is used when you know the element that is to be removed,
whereas you use the pop() to remove an item using its index'''

#---------------------------------------------------------------------------------

#Q7. (index() and count()) 

scores = [85, 92, 78, 92, 65, 92, 88] 

occurance = scores.index(92)
print(f"The first occurance of 92 is at index - {occurance}")

counts = scores.count(92)
print(f"92 appears {counts} times")

score = int(input("Enter a number -"))

if score in scores :
    occur = scores.index(score)
    counted = scores.count(score)
    print(f"{score} is present at index {occur} - ")
    print(f"{score} is present {counted} times")
else :
    print(f"The score {score} doesn't exist in the list.")


#---------------------------------------------------------------------------------

#Q8. (sort() and reverse())

marks = [45, 78, 65, 90, 34, 82, 71] 
print(f"The original list is - {marks}")

marks.sort()
print(f"The list in ascending order is - {marks}")

marks.sort()
marks.reverse()
print(f"The list in descending sorted order is - {marks}")

marks = [45, 78, 65, 90, 34, 82, 71] 
marks.reverse()
print(f"Original list in reversed is - {marks}")

'''sort() - Sorts the list in ascending order
reverse() - Reverses the given string'''

#---------------------------------------------------------------------------------

#Q9. (extend() vs append()) 

list1 = [1, 2, 3] 
list2 = [4, 5, 6] 
list1_copy = list1[:]

print(list1)
print(list2)

list1.extend(list2)
print(f"The list1 after extending with list2 gives - {list1}")

list1_copy.append(list2)
print(f"The copy of list1, after appending with list2 gives - {list1_copy} ")

'''extend() - adds the element of one list to another directly one by one
append() - adds the other list to the main one directly and not its elements'''


#---------------------------------------------------------------------------------

#Q10. (Mini Project - Combined Concepts) 

#    Student Marks Manager 

subject1 = int(input("Enter marks of 1st subject - "))
subject2 = int(input("Enter marks of 2nd subject - "))
subject3 = int(input("Enter marks of 3rd subject - "))
subject4= int(input("Enter marks of 4th subject - "))
subject5 = int(input("Enter marks of 5th subject - "))

marks = [subject1,subject2,subject3,subject4,subject5]
print(f"The marks stored in a list gives = {marks}")

subject6 = 95
marks.append(subject6)

print(f"The highest marks in all subjects combined are - {max(marks)}")
print(f"The lowest marks in all subjects combined are - {min(marks)}")

marks.sort()
print(f"The marks sorted in ascending order are - {marks}")

avg = sum(marks) / (len(marks))
print(f"The average marks are - {avg:.2f}")

print(f"The total number of subjects are - {len(marks)}")


