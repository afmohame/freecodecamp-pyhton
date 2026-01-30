class Category:
    total_balance = 0
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.depo = {"amount": amount, "description": description}
        self.ledger.append(self.depo)
    
    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        withd = {"amount": amount*-1, "description": description}
        self.ledger.append(withd)
        return True
    
    def get_balance(self):
        self.total_balance = sum(i["amount"] for i in self.ledger)
        print(self.total_balance)
        return self.total_balance
    
    def transfer(self, amount, new_category):
        if not self.check_funds(amount):
            return False
        test1 = self.withdraw(amount, f"Transfer to {new_category}")
        if not test1:
            return False

    def check_funds(self, amount):
        if amount > self.depo['amount']:
            return False
        else:
            return True

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
for i in food.ledger:
    print(i)
food.get_balance()
food.get_balance()