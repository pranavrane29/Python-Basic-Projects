### ***# Project 2 — Library Management System***

### ***\*\*Made by:\*\* Pranav Rane***

### ***\*\*Language:\*\* Python 3.x***

### ***\*\*File:\*\* library\_management.py***



\-----------------------------------------------------------------------



##### **## Project Overview**

The Library Management System enables librarians and students to manage book records

within a library. The system tracks books (title, author, ISBN, availability), handles book issue

and return operations, tracks borrowers, and generates availability reports. This project

introduces the concept of nested data structures and state tracking.

\-----------------------------------------------------------------------

##### 

##### **## Data Structure Used**

\*\*Dictionary of Dictionaries\*\* — ISBN (string) serves as the outer key.

Each value is a nested dictionary holding the Books Title ,Books Author,

Issue date, Due Date , Borrowers Name and Id.



Chosen because dictionary lookup by ISBN is **O(1)** — the most frequent

operation in this system is search/update/delete by ISBN, making this

the most efficient structure for the use case.



\----------------------------------------------------------------------



##### **## Functions Used**



add\_book() — Register a new book

issue\_book()     — Issue a book to a student

return\_book()    — Process book return

search\_book()    — Search by title or author

view\_catalog()   — Display full library catalog

check\_due\_date() — Calculate due date from issue date

show\_menu() - Shows operation you can perform



\---------------------------------------------------------------------



##### **## Key Features**

\- Duplicate book prevention on add

\- Per Book adding ISBN Check involved

\- Automatic issued date and due date calculation on issuing a book

\- Borrower details stored on issue, reset to None on return.

\- Input validation via try-except on all numeric inputs

\- Empty record guard on view and search

\- Clean formatted table output for all records



\------------------------------------------------------------------------



##### **## Bonus Feature — Search Book**

Searches Books by:

\- \*\*Title\*\* — Showcases all details of the book

\- \*\*Author\*\* — Returns every books of author(if present).



\------------------------------------------------------------------------



##### **## Resources Used**

\- \*\*Claude (Anthropic)\*\* — Debugging, code review, concept explanations

\- \*\*Google AI / Gemini\*\* — Table formatting syntax reference

\- \*\*Python 3.x Official Documentation\*\* — Standard library reference

\- \*\*Assignment PDF\*\* — Project specification and evaluation criteria



\----------------------------------------------------------------------



##### **## Claude's Honest Account of Contribution**



Pranav built this project independently following the same iterative process as Project 1. Every function was written by him. The core logic — dictionary structure, availability state tracking, issue/return flow, date handling, search logic — is entirely his own work.



**Where Claude contributed:**

Claude explained the datetime module when Pranav didn't know how to handle dates — specifically date.today() and timedelta(days=7). He implemented it correctly himself after the explanation.

Claude caught three structural bugs during review: accessing library\[issue] before checking if the ISBN exists in check\_due\_date(), found = True initialized incorrectly in the author search branch, and due\_date not being reset to None on book return. Pranav fixed all three himself.



Claude identified that library\['available'] = False was updating the wrong dictionary level — the outer library instead of library\[issue] — a nested dictionary access error Pranav caught in his own reasoning before fully writing the fix.



The table formatting in view\_catalog() followed the same pattern established in Project 1, which Pranav applied independently this time without looking it up again.

Bottom line: Project 2 shows measurable improvement over Project 1. Pranav caught his own structural mistakes faster, planned the data structure correctly upfront, and required fewer correction cycles per function. The nested dictionary pattern that confused him in Project 1 is now applied consistently and correctly throughout. **Progress is real.**



\-------------------------------------------------------------------------

&#x09;										— Claude, Anthropic

\*Submitted as part of Python Mini Project Assignment Book | 2025–2026\*

