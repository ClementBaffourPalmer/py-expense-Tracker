project_name = "Ck Palmer Expense Tracker"

def main():
    print(project_name)

if __name__ == "__main__":
   main()


def display_menu():
    print("========== Welcome to Ck Expense Tracker ==========")
    print("1. Add an expense")
    print("2. View expenses")
    print("3. Update an expense")
    print("4. Delete an expense")
    print("5. View expense summary")
    print("6. Exit")
    print("=========================================")


def add_expense():
  # collect expense details from the user
  date = input("Enter date (DD-MM-YYY): ")
  description = input("Enter specification: ")
  amount = input("Enter amount: ")


  # write expense details to CSV file
  with open('expense.txt', mode='a', newline='') as expense_file:
     expenses_writer = csv.writer(expenses_file, delimiter=',')
     expenses_writer.writerow([date, description, amount])

     print("Expense recorded successfully!")



import csv

def view_expenses():
   # read expense deatail from the CSV file
   with open('expenses.txt', mode='r') as expenses_file:
      expenses_reader = csv.reader(expenses_file)
      expenses_reader = list(expenses_reader)


    # Show expense details to user"
   if len(expenses_list) == 0:
         print("No expenses found")
   else: 
       for expense in expenses_list: 
           print(f"Date: {expense[0]}, Description: {expense[1]}, Amount: {expense[2]}")


def update_expenses():
    # Ask expense ID from user
    expense_id = input("Enter expense ID to update")
    date = input("Enter date to update")
    description = input("Enter description to update")
    amount = input("Enter amount to update")
    


