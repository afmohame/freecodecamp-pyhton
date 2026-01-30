class Category:
    total_balance = 0
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.total_balance = amount
        depo = {"amount": amount, "description": description}
        self.ledger.append(depo)
    
    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        withd = {"amount": amount*-1, "description": description}
        self.ledger.append(withd)
        return True
    
    def get_balance(self):
        return sum(i["amount"] for i in self.ledger)
    
    def transfer(self, amount, new_category):
        if not self.check_funds(amount):
            return False
        test1 = self.withdraw(amount, f"Transfer to {new_category}")
        print(test1)
        if not test1:
            return False
        test2 = new_category.deposit(amount, f"Transfer from {self.name}")
        return True
        

    def check_funds(self, amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        else:
            return True

def create_spend_chart(categories):
    pass


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
print("loop")
for i in food.ledger:
    print(i)
print("food.end_total")
print(food.get_balance())
print("food.ledgar")
print(food.ledger)
clothing = Category('Clothing')
food.transfer(50, clothing)