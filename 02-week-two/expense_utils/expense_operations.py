from model import expense
from expense_utils import expense_validator
from datetime import datetime, date

FILE_DIRECTORY = "expenses.csv"

def add_expense(expense_class):
        with open(FILE_DIRECTORY, 'w') as file:
            file.write(f"{expense_class.category},{expense_class.amount},{str(expense_class.date)}\n")

def view_expense():
    try:
          with open(FILE_DIRECTORY, 'r') as file:
               
               criteria = input("What criteria do you want to view? (category, month): ").lower()
               for line in file:
                    if (criteria == "category"):
                         category = input("Enter category: ").lower()
                         if category == line.strip().split(",")[0].lower():
                              print(line.strip().split(","))
                         else:
                              print("No expenses found.")
                    elif (criteria == "month"):
                         month = input("Enter month (YYYY-MM): ")
                         if month == line.strip().split(",")[2][:7]:
                              print(line.strip().split(","))
                         else:
                              print("No expenses found.")
    except:
         raise ValueError("File doesn't exit.")

def total_expenses(category, start_date, end_date):
     total = 0
     with open(FILE_DIRECTORY, 'r') as file:
          for line in file:
               expense_class = expense.Expense(category=line.strip().split(',')[0], expense_amount=line.strip().split(',')[1], expense_date=line.strip().split(',')[2])
               if category != None:
                    if expense_class.category == category:
                         total += int(expense_class.amount)
               elif start_date != None and end_date != None:
                    if expense_validator.check_date(start_date, end_date):
                         if date_converter(expense_class.date) >= start_date and date_converter(expense_class.date) <= end_date:
                              total += int(expense_class.amount)
                    else:
                         total += int(expense_class.amount)
               elif start_date != None:
                    if expense_validator.check_date(start_date=start_date, end_date=end_date):
                         if date_converter(expense_class.date) >= start_date:
                              total += int(expense_class.amount)
               elif end_date != None:
                    if expense_validator.check_date(start_date=start_date, end_date=end_date):
                         if date_converter(expense_class.date) <= end_date:
                              total += int(expense_class.amount)
               else:
                    total += int(expense_class.amount)
     return total
                    
    
def date_converter(date) -> date:
     return datetime.strptime(date, '%Y-%m-%d').date()
