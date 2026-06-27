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


