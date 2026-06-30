### ***# Project 4 — Quiz \& Exam System***

### ***\*\*Made by:\*\* Pranav Rane***

### ***\*\*Language:\*\* Python 3.x***

### ***\*\*File:\*\* QuizSystem.py***

\-----------------------------------------------------------------------



##### **## Project Overview**

The Quiz and Examination System is an interactive Python application that presents multiple

choice questions (MCQs) to a student, evaluates responses, tracks scores, and generates a 

detailed result report at the end. The question bank is stored using tuples (immutable, for data 

integrity) and the application handles timing, scoring, and grade calculation automatically. 

\-----------------------------------------------------------------------

##### 

##### **## Data Structure Used**

\*\*Nested tuples in List - Used this to store the questions in tuple format so that no one can change the question or options.

\*\*List - A Wrong\_list list that counts the wrong answers given by the users.

\----------------------------------------------------------------------



##### **## Functions Used**

• load\_questions()     — Returns the question bank (list of tuples) 

• display\_question()   — Displays a question with options 

• get\_answer() — Accepts and validates student answer        

• evaluate\_quiz() — Scores all answers and compiles result     

• calculate\_grade()    — Returns grade from percentage 

• show\_report()   — Prints final formatted result report 

• show\_wrong\_answers() — Displays incorrectly answered questions 

\---------------------------------------------------------------------



##### **## Key Features**

\- Used nested tuples for immutability of questions

\- Shuffling of the questions on every attempt.

\- Tracks the wrong answers to be displayed at last 

\- Input validation via try-except on all numeric inputs

\- Empty record guard on most methods.

\- Clean interface for quiz (maybe)



\------------------------------------------------------------------------



##### **## Bonus Feature — Shuffle Questions**

The questions are shuffled everytime when someone new 

attempts top do take the quiz.

\------------------------------------------------------------------------



##### **## Resources Used**

\- \*\*Claude (Anthropic)\*\* — Debugging, code review, concept explanations

\- \*\*Python 3.x Official Documentation\*\* — Standard library reference

\- \*\*Assignment PDF\*\* — Project specification and evaluation criteria



\-------------------------------------------------------------------------

&#x09;

\*Submitted as part of Python Mini Project Assignment Book | 2025–2026\*



