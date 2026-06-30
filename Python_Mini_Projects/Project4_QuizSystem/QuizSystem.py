#----------------------------------------------------------------------------------
'''
Project 4 - Quiz & Examination System
Made by Pranav Rane
'''
#----------------------------------------------------------------------------------

'''Functions Definitions followed by actual system.'''



import random # Used to shuffle our questions each time


def load_questions():  # Questions for the quiz is stored here with the Ansers
    questions = [
        ("Which data type is immutable in Python?", "List", "Dictionary", "Tuple", "Set", "C"),
        ("What is the output of print(2 ** 3)?", "6", "8", "9", "12", "B"),
        ("Which keyword is used to define a function in Python?", "func", "define", "def", "function", "C"),
        ("What does len('hello') return?", "4", "5", "6", "error", "B"),
        ("Which of the following is a mutable data type?", "Tuple", "String", "List", "Integer", "C"),
        ("What symbol is used for single-line comments in Python?", "//", "/* */", "#", "--", "C"),
        ("What will type(3.14) return?", "int", "float", "str", "double", "B"),
        ("How do you take input from the user in Python?", "scan()", "cin()", "input()", "readline()", "C"),
        ("What does the append() method do to a list?", "Removes last element", "Adds element at beginning", "Adds element at end", "Sorts the list", "C"),
        ("Which loop is best when number of iterations is already known?", "while", "do-while", "for", "repeat", "C"),
        ("What is the index of the first element in a Python list?", "-1", "1", "0", "None", "C"),
        ("Which function is used to find the length of a list?", "size()", "count()", "len()", "length()", "C"),
    ]
    return questions


def display_question(qno, q): # Used to display the question with their options 
    print(f"Q{qno}: {q[0]}")
    print("OPTIONS - ")
    print(f"  A) {q[1]}")
    print(f"  B) {q[2]}")
    print(f"  C) {q[3]}")
    print(f"  D) {q[4]}")


def get_answer(): # To take answer as an input from the user
    while True:
        try:
            ans = input("Your Answer: ").upper()
            if ans in ["A", "B", "C", "D"]:
                return ans
            else:
                print("Please enter A, B, C or D options only.")
        except Exception:
            print("Invalid input. Try again.")


def calculate_grade(percentage): # Showcases the percentage
    if percentage >= 90:
        return "O"
    elif percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B+"
    elif percentage >= 50:
        return "B"
    else:
        return "F"


def show_wrong_answers(wrong_list): # Displays Wrong answers choosen
    if len(wrong_list) == 0:
        print("\nNo wrong answers. Great job!")
        return

    print("\n--- Wrong Answers Review ---")
    for entry in wrong_list:
        qno = entry[0]
        q = entry[1]
        your_ans = entry[2]
        options = {"A": q[1], "B": q[2], "C": q[3], "D": q[4]}
        correct = q[5]
        print(f"\Q{qno}: {q[0]}")
        print(f"  Your Answer  : {your_ans} - {options[your_ans]}")
        print(f"  Correct Ans  : {correct} - {options[correct]}")


def show_report(name, roll, score, total, wrong_list): # Shows the final report for the quiz
    percentage = (score / total) * 100
    grade = calculate_grade(percentage)

    if percentage >= 50:
        result = "PASS"
    else:
        result = "FAIL"

    print("\n====== QUIZ RESULT ======")
    print(f"Name       : {name}")
    print(f"Roll No    : {roll}")
    print(f"Score      : {score} / {total}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")
    print(f"Result     : {result}") 
    print("===========================")

    show_wrong_answers(wrong_list)


def evaluate_quiz(name, roll, questions): # Initializes the quiz 
    score = 0
    wrong_list = []
    total = len(questions)

    for i in range(total):
        display_question(i + 1, questions[i])
        ans = get_answer()
        correct = questions[i][5]

        if ans == correct:
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! Correct answer was: {correct}")
            wrong_list.append((i + 1, questions[i], ans))

    show_report(name, roll, score, total, wrong_list)


def main(): # main method
    print("=====++++PYTHON QUIZ++++=====")

    name = input("Enter your name: ")

    roll = None
    while roll is None:  # Essential for one time use 
        try:
            roll = int(input("Enter Roll Number: "))
        except ValueError:
            print("Roll number should be an integer.")

    print(f"Student: {name} | Roll: {roll}")

    questions = load_questions()
    random.shuffle(questions)

    print(f"Total Questions Available: {len(questions)}")
    print("Enter choice A, B, C or D for each question.")

    evaluate_quiz(name, roll, questions)

if __name__ == "__main__":
    main()
