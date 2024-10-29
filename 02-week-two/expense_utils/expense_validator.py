from expense_utils.expense_operations import *
from datetime import datetime, date

def validate_date(expense_date, expense_end_date=None):
     try:
          if expense_date != None or expense_date != "":
               if (type(expense_date) is str):
                    expense_date = datetime.strptime(expense_date, '%Y-%m-%d').date()
               
               if check_date(start_date=expense_date, end_date=expense_end_date):
                    return True
               else:
                    return False
          else:
               return False
     except ValueError:
          print("Invalid date format. Please use YYYY-MM-DD.")
          return False
     
               
def check_date(start_date=None, end_date=None):
     if (start_date != "" or start_date != None) and end_date == None:
          if start_date > date.today():
               print("Start date should be less than or equal to today's date.")
               return False
          else:
               return True
     elif (end_date != "" or end_date != None) and start_date == None:
          if end_date > date.today():
               print("End date should be less than or equal to today's date.")
               return False
          else:
               return True
     elif end_date != None or end_date != "" and start_date != None or start_date != "":
          if start_date > end_date:
               print("Start date should be less than or equal to end date.")
               return False
          elif end_date > date.today():
               print("End date should be less than or equal to today's date.")
               return False
          elif end_date < start_date:
               print("End date should be greater than or equal to start date.")
               return False
          else:
               return True
     else:
          return True
    
def amount_validator(amount):
     return f"{amount}".isdigit()

def category_validator(category):
     return f"{category}".isalnum()