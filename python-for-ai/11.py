#------------------------------------------------------------------------------
                        # Task 11
#------------------------------------------------------------------------------


#Q1. (Basic try-except)

try :
    a = int(input("Enter a number -"))
    b = int(input("Enter a number -"))
    print(a/b)
except ValueError:
    print("Only enter a number!")

#------------------------------------------------------------------------------

# Q2. (Handling ZeroDivisionError)


try :
    a = int(input("Enter a number -"))
    b = int(input("Enter a number -"))
    print(a/b)
except ValueError:
    print("Only enter a number!")

except ZeroDivisionError:
    print("Cannot divide by 0!")

#------------------------------------------------------------------------------

#Q3. (Multiple except Blocks)


try :
    a = (input("Enter a number -"))
    b = (input("Enter a number -"))
    c = int(a) # converts an incoming string into int
    d = int(b)
    print(c/d)
except ValueError:
    print("Couldn't convert the input to integer!")

except ZeroDivisionError:
    print("Cannot divide by 0!")


#------------------------------------------------------------------------------

#Q4. (Using else)

try :
    a = int(input("Enter a number -"))
    b = int(input("Enter a number -"))
    print(f"Division - {a/b}")
except ValueError:
    print("Only enter a number!")

except ZeroDivisionError:
    print("Cannot divide by 0!")

else :
    print("Division Performed Successfully!")


#------------------------------------------------------------------------------

#Q5. (Using finally)

try :
    a = int(input("Enter a number -"))
    b = int(input("Enter a number -"))
    print(f"Division - {a/b}")
except ValueError:
    print("Only enter a number!")

except ZeroDivisionError:
    print("Cannot divide by 0!")

finally :
    print("Program execution completed.")

'''Finally is a block of code that comes after try and except 
and always execute whether an exception occures or not'''

#------------------------------------------------------------------------------


# Q6. (Combined try-except-else-finally)


try :
    a = int(input("Enter a number -"))
    b = int(input("Enter a number -"))
    print(f"Division - {a/b}")
except ValueError:
    print("Only enter a number!")

except ZeroDivisionError:
    print("Cannot divide by 0!")

else :
    print("Division Performed Successfully!")

finally :
    print("Thank You for using this division calci~~ : )")

#------------------------------------------------------------------------------

# Q7. (Practical - Age Input)

age = input("Enter your age - ")

try :
    age = int(age)
    
    if age <= 0 :
        raise ValueError
    else :
        print(f"Your age is valid - {age}")

except ValueError :
    print("Age cannot be negative!")

finally :
    print("Code Executed Successfully!")


#-------------------------------------------------------------------------------

# Q.8) Multiple Exception in one block

try :

    num = int(input("Enter a number - "))
    print(f"Dividing 100 by that number gives - {100/num}")

except (ValueError,ZeroDivisionError) :
    print("You either entered something that is not a number, or you tried to divide by 0")


#-------------------------------------------------------------------------------

#Q.9) Debugging Exception Code

'''Incorrect code'''

try # missing colon (:)
    num = int(input("Enter a number: "))
    result = 100/num
    print("Result:", result)
except ValueError # missing colon(:)
    print("Please enter a valid number")

except: # Its better to add zero error in here
    print("Some error occurred") # And print can't divide by zero!

'''Correct code'''


try :
    num = int(input("Enter a number: "))
    result = 100/num
    print("Result:", result)
except ValueError :
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Cannot Divide by zero!")


#-------------------------------------------------------------------------------

# Q.10) Mini Project - Exception handling

# Simple Calculator

while True :
    print("=" * 40)
    print("Welcome to simple calculator!")
    print("Enter 2 numbers for our operations -")
    try :
        a = float(input("Enter number 1 -"))
        b = float(input("Enter number 2 -"))
        print("Here is a menu of what you can do - ")
        print("1)Addition")
        print("2)Subtraction")
        print("3)Multiplication")
        print("4)Division")
        print("5)Exit")

        choice = int(input("What do you want to do (1 - 5) - "))

        if choice == 1:
            add = a + b 
            print(f"Addition - {add}")
            
        elif choice == 2 :
            sub = a - b
            print(f"Subtraction - {sub}")

        elif choice == 3 :
            mul = a * b
            print(f"Multiplication - {mul}")

        elif choice == 4 :
            if b == 0 :
                raise ZeroDivisionError
            else :
                div = a / b 
                print(div)
        elif choice == 5 :
            print("Exiting...")
            break
        else :
            print("Pls enter between 1 to 5!")

    except ValueError:
        print("Enter valid numbers only!")
    except ZeroDivisionError :
        print("Cannot Divide by zero!")

    finally :
        print("Operation Attempted!")