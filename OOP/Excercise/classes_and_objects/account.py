class Account:

    def __init__(self, id: int, name: str, balance: int = 0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount):
        pass

    def debit(self,amount):
        pass

    def info(self):
        return f"User {name} with account {id} has {balance} balance"