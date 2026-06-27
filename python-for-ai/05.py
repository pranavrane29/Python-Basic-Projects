
#Q1. (String Indexing)

string = input("Enter any String -")

print(f"The first character in your string is- {string[0]}")
print(f"The last character in your string is- {string[-1]}")
print(f"The third character from yourstring is - {string[2]}")
print(f"The second character from yourstring-end is - {string[-2]}")

'''Positive Indexing - Indexing from the starting of string
that goes on as
0,1,2,3 ..... n storing each string elements

Negative Indexing - Indexing from the starting of string
that goes on as

0,1,2,3 ..... n storing each string elements.'''


#Q2 

string = input("Enter any String -")

print(f"The first 5 characters in your string - {string} are - {string[0:6]}")

print(f"The last 4 characters in your string - {string} are ->{string[-4:]}")

print(f"The entered string in reveresed order is -{string[-1 ::- 1]}")
print(f"Every 2nd character of the string is - {string[0 :: 2]}")

'''slice[start:end:step] -- > i)start indicates the starting value
index(inclusive)

ii)stop indicates the stopping index(Exclusive)

iii)step indicates the elements its going to skip and print'''


#Q3

main_string = "Hello World"
sub_string = "Hello"

if (sub_string in main_string) : # String is case sensitive
  print("Substring found in the Mainstring")
else :
  print("Substring not found!")

#-----------------------------------------------------------------------------------------

#Q4. (len() Function)

string = input("Enter any String - ")
print(f"The length of the entered string is - {len(string)}")
print(f"The last character of the entered string is - {string[len(string)-1]}")

if len(string) % 2 != 0 :
  middle = len(string) // 2
  print(f"The middle character is - {string[middle]}")
else :
  print("The number is Even")

'''Users assume len() gives the value of the indexes but instead it gives the total characters of the
string, including whitespace'''

#-----------------------------------------------------------------------------------------

#Q5. (range() - Basic Forms)

#a)
for i in range(0,11) :
  print(i)

#b)
for i in range(5,16) :
  print(i)

#c)
for i in range(1,22,2) :
  print(i)

'''range(start,stop,step)--> i)start indicates the starting position of a element 
ii)stop indicates the stopping point of the range(exclusive)
iii)step indicates the elements it will skip and print '''

#-----------------------------------------------------------------------------------------

#Q6. (range() with Negative Step)

print("Numbers from 20 down to 10 - ")
for i in range(20,9,-1) :
  print(i)

print("Numbers from 15 down to 1 in steps of 2. -")
for i in range(15,0,-2) :
  print(i)

#-----------------------------------------------------------------------------------------

#Q7. (Combined: Strings + range())

string = input("Enter a string - ")

index = 0
length = len(string)
print("Each character of the string one by one (with its index). - ")
for i in range(length):
  print(f"{string[i]} at index - {index}")
  index += 1

print("The string in reverse order using negative step in range(). - ")
for i in range(length-1,-1,-1) :
    print(f"The string in reversed order is - {string[i]}")
    
#-----------------------------------------------------------------------------------------

#Q8. (Membership with range())

number = int(input("Enter any number - "))

if number in range(1,51) and number in range(10,100,5) :
  print("The number is present in range(1, 51) and in range(10, 100, 5).")
else :
  print("The number is not present in either range(1,51) or range(10,100,5)")

#-----------------------------------------------------------------------------------------

#Q9. (Slicing + range())

print("The first 10 even numbers are - ")
for i in range(2,21,2) :
  print(i)

print("Numbers from 1 to 30 in steps of 3 - ")
for i in range(1,31,3) :
  print(i)

strr = "PythonProgramming"

print(strr[0:6])
print(strr[6:17])
print(f"The PythonProgramming in reversed is - {strr[-1::-1]}")

#-----------------------------------------------------------------------------------------

#Q10. (Mini Project - Combined)

#String Analyazer

string_input = input("Enter a string - ")

def ret_length(string) :
  print(f"The length of the enetered string is - {len(string)}")
  print("_ "*30)

def slicing(string) :
  mid = len(string) // 2
  print(f"First half - {string[:mid]}") 
  print(f"Second half - {string[mid:]}") 
  print("_ "*30)


def check(string) :
  if "python" == string.lower() :
    print("Python word is present in our string ")
    print("_ "*30)

  else :
    print("Python word is not present in our string")
    print("_ "*30)


def index(string) :
 print("String with its positive indices")
 index = 0
 for i in range(len(string)) :
   print(f"{string[i]} at index - {index}")
   index += 1

 print("String with its negative indices")
 index = -1
 for i in range(-1,-len(string)-1,-1) :
   print(f"{string[i]} at index - {index}")
   index -= 1
 print("_ "*30)

def reverse(string):
  reversed = string[-1::-1]
  print(f"The string in reverse is - {reversed}")
 


ret_length(string_input)
check(string_input)
index(string_input)
reverse(string)
