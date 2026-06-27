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

