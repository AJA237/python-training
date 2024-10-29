from expense_utils import expense_validator, expense_operations
from model import expense
from datetime import date

def run():
     isRunning = True
     print("\nWelcome to the Expense Tracker.\n")
     while isRunning:
          operation = input("What operation will you like to carry out?\n1. Add Expense\n2. View Expenses\n3. Total Expenses\n4. Exit\n>>> ")
          if operation == "1":
               category = input("Enter category: ")
               if expense_validator.category_validator(category):
                    amount = input("Enter amount: ")
                    if expense_validator.amount_validator(amount):
                         expense_operations.add_expense(category, amount)
                         print("Expense added successfully.\n")
                    else:
                         print("Invalid amount. Please try again.\n")
                         continue
               else:
                    continue
          elif operation == "2":
               expense_operations.view_expense()
          elif operation == "3":
               category = input("Enter category (optional): ")
               start_date = input("Enter start date (YYYY-MM-DD) (optional): ")
               end_date = input("Enter end date (YYYY-MM-DD) (optional): ")
               if category == "" and start_date == "" and end_date == "":
                    print(f"Total expenses: {expense_operations.total_expenses(category=None, start_date=None, end_date=None)}")
               elif category != "" and start_date == "" and end_date == "":
                    print(f"Total expenses: {expense_operations.total_expenses(category=category, start_date=None, end_date=None)}")
               elif category == "" and start_date != "" and end_date == "":
                    if expense_validator.validate_date(start_date):
                         print(f"Total expenses: {expense_operations.total_expenses(category=None, start_date=expense_operations.date_converter(start_date), end_date=date.today())}")
               elif category == "" and start_date == "" and end_date != "":
                    if expense_validator.validate_date(end_date):
                         print(f"Total expenses: {expense_operations.total_expenses(category=None, end_date=expense_operations.date_converter(end_date), start_date=None)}")
               elif expense_validator.validate_date(expense_date=start_date) and expense_validator.validate_date(end_date):
                    if start_date == "" and end_date == "":
                         print(f"Total expenses: {expense_operations.total_expenses(category=category, start_date=None, end_date=None)}")
                    elif start_date == "" and end_date != "":
                         print(f"Total expenses: {expense_operations.total_expenses(category=category, start_date=None, end_date=expense_operations.date_converter(end_date))}")
                    elif start_date != "" and end_date == "":
                         print(f"Total expenses: {expense_operations.total_expenses(category=category, start_date=expense_operations.date_converter(start_date), end_date=None)}")
                    else:
                         print(f"Total expenses: {expense_operations.total_expenses(category=category, start_date=expense_operations.date_converter(start_date), end_date=expense_operations.date_converter(end_date))}")
               else:
                    print("Invalid date format. Please use YYYY-MM-DD.\n")
          elif operation == "4":
               isRunning = False
          else:
               print("Invalid operation. Please try again.\n")