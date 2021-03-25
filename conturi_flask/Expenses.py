
class Expense:

    def __init__(self, id, label, amount):
        self.id = id
        self.label = label
        self.amount = amount

    def to_json(self):
        return {'id': self.id, 'first_name': self.label,
                'label': self.label, 'amount': self.amount}


class ExpenseService:

    def __init__(self):
        self.expenses = [
            Expense(1, 'Food', 10),
            Expense(2, 'Water', 5)
        ]

    def get_expenses(self):
        return self.expenses

    def id_exists(self, id):
        for expense in self.expenses:
            if expense.id == id:
                return True
        return False

    def add_expense(self, id, label, amount):
        new_expense = Expense(id, label, amount)
        self.expenses.append(new_expense)

    def update_expenses(self, id, label, amount):
        expense_index = 0
        for index, expense in enumerate(self.expenses):
            if expense.id == id:
                expense_index = index

        self.expenses[expense_index].label = label
        self.expenses[expense_index].amount = amount

    def delete_expense(self, id):
        expense_index = 0
        for index, expense in enumerate(self.expenses):
            if expense.id == id:
                expense_index = index

        self.expenses.pop(expense_index)

    def get_expense(self, id):
        expense_index = 0
        for index, expense in enumerate(self.expenses):
            if expense.id == id:
                expense_index = index

        return self.expenses[expense_index]
