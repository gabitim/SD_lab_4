
class Cont:

    def __init__(self, id, first_name, last_name, amount):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.amount = amount

    def to_json(self):
        return {'id': self.id, 'first_name': self.first_name,
                'last_name': self.last_name, 'amount': self.amount}


class ContService:

    def __init__(self):
        self.conturi = [
            Cont(1, 'Gabi', 'Timofti', 100),
            Cont(2, 'Mihai', 'Lara', 150)
        ]

    def get_conturi(self):
        return self.conturi

    def id_exists(self, id):
        for cont in self.conturi:
            if cont.id == id:
                return True
        return False

    def add_cont(self, id, first_name, last_name, amount):
        cont_nou = Cont(id, first_name, last_name, amount)
        self.conturi.append(cont_nou)

    def update_cont(self, id, first_name, last_name, amount):
        account_index = 0
        for index, cont in enumerate(self.conturi):
            if cont.id == id:
                account_index = index

        self.conturi[account_index].first_name = first_name
        self.conturi[account_index].last_name = last_name
        self.conturi[account_index].amount = amount

    def delete_cont(self, id):
        account_index = 0
        for index, cont in enumerate(self.conturi):
            if cont.id == id:
                account_index = index

        self.conturi.pop(account_index)

    def get_cont(self, id):
        account_index = 0
        for index, account in enumerate(self.conturi):
            if account.id == id:
                account_index = index

        return self.conturi[account_index]
