from datetime import date

class Expense:
    def __init__(self, category, expense_amount, expense_date=date.today()):
        self.category = category
        self.amount = expense_amount
        self.date = expense_date

    def __str__(self):
        return f"Category: {self.category}, Amount: {self.amount}, Date: {self.date}"

    