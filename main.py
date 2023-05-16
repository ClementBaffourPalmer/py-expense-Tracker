import csv
project_name = "Ck Palmer Expense Tracker"


underline = "================================="

def main():
    print(underline)
    print(project_name)
    print(underline)
    display_menu()
    print(underline)
    
    # check if file exits,
    # if file exits --> open in write mode
    # else open in append mode
    file = open("expenses.csv", "w")

    choice = -1 
    while choice != 0:
     choice =int(input("what do you want to do: "))
    print("You want to do choice:", choice)

    # conditions ===> if,   elif, else 
    if choice == 1:
       add_expense(file)

if __name__ == "__main__":
   main()


def display_menu():
    print("========== Welcome to Ck Expense Tracker ==========")
    print("1. Add an expense")
    print("2. View expenses")
    print("3. Update an expense")
    print("4. Delete an expense")
    print("5. View expense summary")
    print("6. Exit Application")
    print("0. ========= Exit Application ===========")
    # ...

def add_expense(file):
  # collect expense details from the user
  title = input("what should I call this expense? ==>")
  date = input("Enter date (DD-MM-YYY): ")
  description = input("Enter specification: ")
  amount = input("Enter amount: what is the amount in Ghc")

  print("Title:\t", title)
  print("Date:\t", date)
  print("description:\t", description)

  yes_or_no = input("confirm you want to add this expense: yes(y)/no(n) ==>")

  if yes_or_no == "yes" or "YES" or "y" or "Y":
     print("persisting to db...")
     # add to the csv file 
     writer = csv.writer(file)
     writer.writerow([title, amount, description])
     print("Added to db")
     print(underline)
  else:
    print("Aborted...")
 
  # write expense details to CSV file
  with open('expense.txt', mode='a', newline='') as expense_file:
     expenses_writer = csv.writer(expense_file, delimiter=',')
     expenses_writer.writerow([date, description, amount])

     print("Expense recorded successfully!")

  
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

    expense_id = input("Enter expense ID to update: ")
    new_date = input("Enter new date (DD-MM-YYY): ")
    new_desc = input("Enter new description: ")
    new_amount = input("Enter new amount: ")
    




