#----------------------------------------------------------------------------------
'''
Project 2 - Library Management System
Made by Pranav Rane
'''
#----------------------------------------------------------------------------------

'''Functions Definitions followed by actual system.'''


from datetime import date,timedelta

def add_book() : #Add book in collection
    try :
            
        isbn = input("Enter the ISBN of the book - ")
        if isbn in library :
            print("A book with this ISBN already exists!")
        else :
            title = input("Enter the title of the book - ")
            author = input("Enter the authors name - ")
            print("Book added successfully!")
            library[isbn] = {
                    "title" : title,
                    "author" : author,
                    "available" : True,
                    "borrower_name" : None,
                    "borrower_id" : None,
                    "issue_date" : None,
                    "due_date" : None
                }
    except Exception:
        print("Something Unexpected happened!")


def issue_book() : # Issue book
    try :

        issue = input("Enter the ISBN to get the book!")
        if issue in library :
            if library[issue]['available'] == True :
                print("The book is available to be issued!")
                library[issue]['available'] = False
                name = input("Enter your name - ")
                library_id = int(input("Enter your library id - "))
                library[issue]['borrower_name'] = name
                library[issue]['borrower_id'] = library_id
                today = date.today()
                library[issue]['issue_date'] = today
                due_date = today + timedelta(days=7)
                print(f"You need to return the book by - {due_date}")
                print(f"You, {library[issue]['borrower_name']} have successfully borrowed the book!")
                library[issue]["due_date"] = due_date
            
            else :
                print("The book is unavailable to be borrowed! ")
    
        else :
            print("The book with this ISBN isn't available in our library!")    
    except ValueError :
        print("Pls enter correct value!")


def return_book() : #Returns a book
    try :
        issue = input("Enter the ISBN of book to be returned - ")
        if issue in library:
            if library[issue]['available'] == True :
                print("The book was not issued!")
            else :
                library[issue]['borrower_name'] = None
                library[issue]['borrower_id'] = None
                library[issue]['issue_date'] = None
                library[issue]['due_date'] = None
                library[issue]['available'] = True
                print("The book was returned successfully!")
        else:
            print("The book doesn't belong to this library")        
    except ValueError:
        print("Pls enter correct values!")

def view_catalog() : # Showcases all books(if available)
    if not library:
        print("No books to showcase!")
    else :
        fmt = "{:<20} {:<15} {:<15} {:<8}"
        print("=" * 70)
        print(fmt.format("ISBN", "Title", "Author", "Available"))
        print("=" * 70)
        
        for key,details in library.items() :
            print(fmt.format(
                key,
                details["title"],
                details["author"],
                "Yes" if details["available"] else "No",
            ))
        print("=" * 70)


def check_due_date() : # Checks due date using issued date
    try : 
        issue = input("Enter the ISBN of the book - ")
        if issue not in library:
          print("This book was not issued from our library!")
        else :
            if library[issue]['available'] == True :
                print("The Book was not issued!")
            else : 
                print(f"The due date of your borrowed book is - {library[issue]['due_date']}")
    except ValueError :
        print("Enter correct value!")


def search_book(): #Bonus Task -- Searches Books by author or title
    try :
        if not library:
            print("No books to showcase!")
        else :
            choice = input("Do you want to search a specific book or books issued by a author(type Title or Author) - ").lower()
            if choice == 'title' :
                title = input("Enter the title of the book - ").lower()
                found = False
                for isbn,details in library.items():
                    if title == details['title'].lower() :
                        found = True 
                        print("\n" + "=" * 50)
                        print(f"       BOOK DETAILS FOUND (ISBN: {isbn})")
                        print("=" * 50)
                        print(f" Title:        {details['title']}")
                        print(f" Author:     {details['author']}")
                        print(f" Available:  {"YES" if{details['available']} else "NO"}")                  
                        print(f" Issued on :  {details['issue_date']}")
                        print(f" Due Date :     {details['due_date']}")
                        print(f"Borrower id(if borrowed) : {details['borrower_id']}")
                        print("=" * 40)
                if not found :
                    print("No book found with such Title!")
            elif choice == 'author':
                name = input("Enter the Author's name - ").lower()
                found = False
                for isbn,details in library.items():
                    if name  == details['author'].lower() :
                        found = True 
                        print("\n" + "=" * 50)
                        print(f"       FOUND AUTHOR'S BOOK'S      ")
                        print("=" * 50)
                        print(f" Title:        {details['title']}")
                        print(f" Available:  {"YES" if{details['available']} else "NO"}")                  
                        print(f" Issued on :  {details['issue_date']}")
                        print(f" Due Date :     {details['due_date']}")
                        print(f"Borrower id(if borrowed) : {details['borrower_id']}")
                        print("=" * 40)
                if not found :
                    print("No Author Books found!")
            else :
                print("Pls enter only author or title!")
    except ValueError:
        print("Pls enter correct values!")


def show_menu() : #Shows what you can perform
    print("What you can perfrom - ")
    print("1)Register a new book")
    print("2)Issue a book to a student")
    print("3)Return a Book")
    print("4)View all books")
    print("5)Check the due date for a certain book")
    print("6)Search a book by its author or title.")
    print("7)Exit...")


'''Actual System Below '''

library = {} # Will store all data 

def main() :
    while True :
        try :
            print("-" * 58)
            print("_____Welcome to Library Management System!_____")
            print("Note - Asks for user input to perform a specific action.")
            print("-" * 58)

            show_menu()

            choice = input("Enter what you want to do (1 - 7) - ")
            print("-" * 30)
            if choice == "1" :
                add_book()
            elif choice == "2" :
                issue_book()
            elif choice == "3" :
                return_book()
            elif choice == "4" :
                view_catalog()
            elif choice == "5" :
                check_due_date()
            elif choice == "6" :
                search_book()
            elif choice == "7" :
                print("Exiting Program....")
                break
            else :
                print("Pls enter a valid choice(1 - 7)")
        except ValueError :
            print("Enter correct value!")


if __name__ == "__main__":
    main()