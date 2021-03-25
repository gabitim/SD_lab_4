from flask import Flask, render_template, request, redirect

from Cont import ContService
from Expenses import ExpenseService

app = Flask(__name__)

cont_service = ContService()
expense_service = ExpenseService()


@app.route('/')
@app.route('/index')
def index():
    global cont_service
    accounts = cont_service.get_conturi()
    expenses = expense_service.get_expenses()
    return render_template('index.html', accounts=accounts, expenses=expenses)


@app.route('/addCont', methods=['POST'])
def addCont():
    global cont_service

    if request.method == 'POST':
        form = request.form
        Id = int(form.get('id'))
        first_name = form.get('first_name')
        last_name = form.get('last_name')
        balance = form.get('amount')

        if not cont_service.id_exists(Id):
            cont_service.add_cont(Id, first_name, last_name, balance)
            return redirect('/')

    return render_template("error_duplicat.html")


@app.route('/updateCont', methods=['POST', 'PUT'])
def updateCont():
    global cont_service

    if request.method in ['PUT', 'POST']:
        form = request.form
        Id = int(form.get('id'))
        first_name = form.get('first_name')
        last_name = form.get('last_name')
        amount = form.get('amount')

        if cont_service.id_exists(Id):
            cont_service.update_account(Id, first_name, last_name, amount)
            return redirect('/')

    return render_template("error_cont.html")


@app.route('/deleteCont', methods=['POST', 'DELETE'])
def deleteCont():
    global cont_service

    if request.method in ['DELETE', 'POST']:
        form = request.form
        Id = int(form.get('id'))

        if cont_service.id_exists(Id):
            cont_service.delete_cont(Id)
            return redirect('/')

    return render_template("error_cont.html")


@app.route('/getCont', methods=['GET', 'POST'])
def getCont():
    global cont_service

    if request.method in ['GET', 'POST']:
        Id = int(request.args.get('id'))
        if cont_service.id_exists(Id):
            cont = cont_service.get_cont(Id)
            return render_template('show_cont.html', cont=cont)

    return render_template("error_cont.html")


# expenses
@app.route('/addExpense', methods=['POST'])
def addExpense():
    global expense_service

    if request.method == 'POST':
        form = request.form
        Id = int(form.get('id'))
        label = form.get('label')
        amount = form.get('amount')

        if not expense_service.id_exists(Id):
            expense_service.add_expense(Id, label, amount)
            return redirect('/')

    return render_template("error_duplicat.html")


@app.route('/updateExpense', methods=['POST', 'PUT'])
def updateExpense():
    global expense_service

    if request.method in ['PUT', 'POST']:
        form = request.form
        Id = int(form.get('id'))
        label = form.get('label')
        amount = form.get('amount')

        if cont_service.id_exists(Id):
            expense_service.update_expense(Id, label, amount)
            return redirect('/')

    return render_template("error_cont.html")


@app.route('/deleteExpense', methods=['POST', 'DELETE'])
def deleteExpense():
    global expense_service

    if request.method in ['DELETE', 'POST']:
        form = request.form
        Id = int(form.get('id'))

        if expense_service.id_exists(Id):
            expense_service.delete_expense(Id)
            return redirect('/')

    return render_template("error_cont.html")


@app.route('/getExpense', methods=['GET', 'POST'])
def getExpense():
    global expense_service

    if request.method in ['GET', 'POST']:
        Id = int(request.args.get('id'))
        if expense_service.id_exists(Id):
            cont = expense_service.get_expense(Id)
            return render_template('show_expense.html', cont=cont)

    return render_template("error_cont.html")


if __name__ == '__main__':
    app.run(debug=True)
