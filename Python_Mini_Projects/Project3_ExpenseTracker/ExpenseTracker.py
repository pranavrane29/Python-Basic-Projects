#----------------------------------------------------------------------------------
'''
Project 3 - Expense Tracker System
Made by Pranav Rane
'''
#----------------------------------------------------------------------------------

'''Functions Definitions followed by actual system.'''

from datetime import datetime

def add_expense(): #add expenses made
    try:
        description = input("Describe the expense: ")
        category = input("Category of the expense: ")
        date = input("Date of expense (DD-MM-YYYY): ")
        # validate date format early
        try:
            datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            print("Date must be in DD-MM-YYYY format.")
            return

        amount = float(input("Enter the amount you spent: "))
        if amount <= 0:
            print("You cannot make negative or zero expenses!")
            return

        expenses.append({
            "desc": description,
            "category": category,
            "amount": amount,
            "date": date
        })
        print("Expense added successfully!")

    except ValueError:
        print("Please enter correct values (amount must be a number).")


def view_expenses(): # shows all expenses made
    if not expenses:
        print("No expenses made!")
    else:
        for index, expense in enumerate(expenses, start=1):
            print(f"{index}) {expense['desc']}")
            print("Expenses made for this -")
            print(f"Category - {expense['category']}")
            print(f"Amount - Rs.{expense['amount']:.2f}")
            print(f"Date - {expense['date']}")
            print("=" * 30)


def category_summary(): # showcases category-wise spending
    if not expenses:
        print("No expenses made!")
        return

    c_summary = {}
    for expense in expenses:
        cat = expense["category"]
        c_summary[cat] = c_summary.get(cat, 0.0) + expense["amount"]

    print("Category-wise summary:")
    for category, total in c_summary.items():
        print(f"{category}: Rs. {total:.2f}")


def budget_report(budget): # Cslcukate budget report
    total_spent = sum(exp["amount"] for exp in expenses)
    print(f"Total spent: Rs.{total_spent:.2f}")
    print(f"Budget: Rs.{budget:.2f}")
    if total_spent > budget:
        print("WARNING!! - You have exceeded your budget!")
    else:
        remaining = budget - total_spent
        used_pct = (total_spent / budget) * 100 if budget > 0 else 0
        print(f"You are within budget. Remaining: Rs.{remaining:.2f}")
        if used_pct >= 100:
            print("You have used 100% of your budget(overbudget).")
        elif used_pct >= 80:
            print(f"WARNING: You have used {used_pct:.2f}% of your budget (>=80%).")
        else:
            print(f"Budget used: {used_pct:.2f}%.")


def top_category(): # most expensive category 
    if not expenses:
        print("No expenses made yet.")
        return

    summary = {}
    for exp in expenses:
        category = exp["category"]
        summary[category] = summary.get(category, 0.0) + exp["amount"]

    top = max(summary, key=summary.get)
    print(f"Top Category: {top} (Rs.{summary[top]:.2f})")


def most_expensive(): #calculate the most expensive purchase made
    if not expenses:
        print("No expenses recorded yet.")
    else:
        max_exp = max(expenses, key=lambda x: x["amount"])
        print(f"Most expensive expense: {max_exp['desc']} | Rs.{max_exp['amount']:.2f} | {max_exp['date']}")


def average_daily_spending(): #bonus task
    if not expenses:
        print("No expenses made!.")
        return

    dates = []
    for exp in expenses:
        try:
            d = datetime.strptime(exp["date"], "%d-%m-%Y").date()
            dates.append(d)
        except ValueError:
            print("Enter correct date!")
            continue

    if not dates:
        print("No valid dates found in expenses.")
        return

    min_date = min(dates)
    max_date = max(dates)
    days_span = (max_date - min_date).days + 1  
    total_spent = sum(exp["amount"] for exp in expenses)

    avg_per_day = total_spent / days_span if days_span > 0 else total_spent
    print(f"Expense date range: {min_date.strftime('%d-%m-%Y')} to {max_date.strftime('%d-%m-%Y')} ({days_span} day(s))")
    print(f"Total spent: Rs.{total_spent:.2f}")
    print(f"Average daily spending over this range: Rs.{avg_per_day:.2f}")


def show_menu():
    print("\nWhat you can perform - ")
    print("1) Add Expense")
    print("2) View all expenses")
    print("3) See total expense for each category (summary)")
    print("4) Calculate your Budget Report")
    print("5) Find the most expensive single expense")
    print("6) Show top spending category")
    print("7) Calculate average daily spending")
    print("8) Exit")


'''Actual System Below '''

expenses = []  # globally stores 


def main():
    try:
        budget = float(input("Set your monthly budget: "))
        if budget <= 0:
            print("Budget must be positive!")
            return

        while True:
            print("\n_____Welcome to Budget Tracker_____")
            show_menu()
            choice = input("Enter what you want to do (1-8) - ")

            if choice == "1":
                add_expense()
            elif choice == "2":
                view_expenses()
            elif choice == "3":
                category_summary()
            elif choice == "4":
                budget_report(budget)
            elif choice == "5":
                most_expensive()
            elif choice == "6":
                top_category()
            elif choice == "7":
                average_daily_spending()
            elif choice == "8":
                print("Exiting...")
                break
            else:
                print("Enter valid choice only (1-8)!")
    except ValueError:
        print("Please enter correct values for budget.")


if __name__ == "__main__":
    main()
