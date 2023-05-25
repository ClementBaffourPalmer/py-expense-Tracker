import csv
from terminaltables import AsciiTable

project_name = "Ck Palmer Expense Tracker"
underline = "================================="


def display_menu():
    print("========== Welcome to Ck Expense Tracker ==========")
    print("1. Adding an expense")
    print("2. View expenses")
    print("3. Update an expense")
    print("4. Delete an expense")
    print("5. View expense summary")
    print("6. Exit Application")


def add_expense(file):
    # collect expense details from the user
    title = input("What should I call this expense? ==> ")
    amount = input("What is the amount (Ghs)? ==>")
    description = input("Enter some description (optional) ==>")

    print("Title:\t", title)
    print("Description:\t", description)
    print("Adding Expenses")

    data = [title, amount, description]
    table_data = [["Title", "Amount", "Description"], data]
    table = AsciiTable(table_data)
    print(table.table)
    yes_or_no = input("Confirm you want to add this expense (yes/no): ")

    if yes_or_no.lower() in ["yes", "y"]:
        print("Persisting to database...")
        # add to the csv file
        writer = csv.writer(file)
        writer.writerow(data)
        print("Added to db")
        print("Expense recorded successfully!")
        print(table.table)
        print(underline)
    else:
        print("Aborted...")


def view_expenses(file):
    with open('expenses.csv', mode='r') as file:
        reader = csv.reader(file)
        expenses = list(reader)

    if len(expenses) == 0:
        print("No expenses found")
    else:
        print("Expense Details:")
        table_data = [["Title", "Amount", "Description"]]
        table_data.extend(expenses)
        table = AsciiTable(table_data)
        print(table.table)


def update_expenses(file):
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
        expenses = list(reader)

    found = False
    for i, expense in enumerate(expenses):
        if expense[0] == expense_id:
            found = True
            del expenses[i]
            print("Expense deleted successfully!")
            break

    if not found:
        print("Expense not found")

    with open('expenses.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(expenses)

def view_expense_summary():
    with open('expenses.csv', mode='r') as file:
        reader = csv.reader(file)
        expenses = list(reader)

    if len(expenses) == 0:
        print("No expenses found")
    else:
        total_expenses = 0
        table_data =[["Title", "Amount"]]

        for expense in expenses:
            title, *data = expense
            amount = data[0]
            try:
                amount = float(amount)
                total_expenses += amount
                table_data.append([title, amount])
            except ValueError:
                table_data.append([title, "Invalid amount"])

    table = AsciiTable(table_data)
    print(table.table)
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

    choice = -1
    while choice != 0:
        choice = int(input("What do you want to do: "))
        print("Your option:", choice)

        if choice == 1:
            add_expense(file)
        elif choice == 2:
            view_expenses(file)
        elif choice == 3:
            update_expenses(file)
        elif choice == 4:
            delete_expense()
        elif choice == 5:
            view_expense_summary()
        elif choice == 6:
            exit_application()
        elif choice == 0:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
