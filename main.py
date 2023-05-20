import csv

project_name = "Ck Palmer Expense Tracker"
underline = "================================="

def display_menu():
    print("========== Welcome to Ck Expense Tracker ==========")
    print("1. Add an expense")
    print("2. View expenses")
    print("3. Update an expense")
    print("4. Delete an expense")
    print("5. View expense summary")
    print("6. Exit Application")
  

def add_expense(file):
    # collect expense details from the user
    title = input("What should I call this expense? ==> ")
    date = input("Enter date (DD-MM-YYYY): ")
    description = input("Enter specification: ")
    amount = input("Enter amount in Ghs: ")

    print("Title:\t", title)
    print("Date:\t", date)
    print("Description:\t", description)

    yes_or_no = input("Confirm you want to add this expense (yes/no): ")

    if yes_or_no.lower() in ["yes", "y"]:
        print("Persisting to database...")
        writer = csv.writer(file)
        writer.writerow([title, date, description, amount])
        print("Expense recorded successfully!")
    else:
        print("Aborted...")

def view_expenses():
    with open('expenses.csv', mode='r') as file:
        reader = csv.reader(file)
        expenses = list(reader)

    if len(expenses) == 0:
        print("No expenses found")
    else:
        print("Expenses:")
        for expense in expenses:
            print(f"Title: {expense[0]}, Date: {expense[1]}, Description: {expense[2]}, Amount: GHS {expense[3]}")

def update_expenses(expenses_file):
    expense_id = input("Enter the expense ID to update: ")

    with open('expenses.csv', mode='r') as file:
        reader = csv.reader(file)
        expenses_list = list(reader)

    found = False
    for i, expense in enumerate(expenses_list):
        if expense[0] == expense_id:
            found = True
            new_date = input("Enter new date (DD-MM-YYYY): ")
            new_description = input("Enter new description: ")
            new_amount = input("Enter new amount in Ghc: ")

            yes_or_no = input("Confirm you want to update this expense (yes/no): ")

            if yes_or_no.lower() in ["yes", "y"]:
                expenses_list[i] = [expense_id, new_date, new_description, new_amount]
                print("Expense updated successfully!")
            else:
                print("Aborted...")
            break

    if not found:
        print("Expense not found")

    with open('expenses.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(expenses_list)

def delete_expense():
    expense_id = input("Enter expense ID to delete: ")

    with open('expenses.csv', mode='r') as file:
        reader = csv.reader(file)
        expense = list(reader)

    found = False
    for i, expense in enumerate(expense):
        if expense[0] == expense_id:
            found = True
            del expense[i]
            print("Expense deleted successfully!")
            break

    if not found:
        print("Expense not found")

    with open('expenses.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(expense)

def view_expense_summary():
    with open('expenses.csv', mode='r') as file:
        reader = csv.reader(file)
        expenses = list(reader)

    if len(expenses) == 0:
        print("No expenses found")
    else:
        total_expenses = 0
        print("Expense Summary:")
        for expense in expenses:
            title, date, description, amount = expense
            amount = float(amount)
            total_expenses += amount
            print(f"Title: {title}, Amount: {amount}")

        print("Total Expenses:", total_expenses)

def exit_application():
    print("Exiting the application...")

def main():
    print(underline)
    print(project_name)
    print(underline)
    display_menu()
    print(underline)
    
    file = open("expenses.csv", "a", newline='')

    range = -1
    while range != 0:
        range = int(input("What do you want to do: "))
        print("Your option:", range)
        
        if range == 1:
            add_expense(file)
        elif range == 2:
            view_expenses()
        elif range == 3:
            update_expenses(file)
        elif range == 4:
            delete_expense()
        elif range == 5:
            view_expense_summary()
        elif range == 6:
            exit_application()
        elif range == 0:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
