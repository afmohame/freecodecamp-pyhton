#smarter_main.py is a better code made with using online resource while main.py 
#is my first try without relying on the internet
class Category:
    total_balance = 0
    max_chars = 30
    symbol = "*"
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

        test1 = self.withdraw(amount, f"Transfer to {new_category.name}") #self here references food object
        if not test1:
            return False
        new_category.deposit(amount, f"Transfer from {self.name}") #here we deposited the amount to the clothing object balance
        #test1 = self.withdraw(amount, f"Transfer to {new_category.name}") creates a new object which when we call
        #print(food) the __str__ will also print clothing objects length so we need to add add .name
        return True
        

    def check_funds(self, amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        else:
            return True

    def __str__(self):
        symbols_number = (self.max_chars - len(self.name))
        left = symbols_number//2 # // will throw the decimal away 
        right = symbols_number - left
        template = f"{'*'*left}{self.name}{'*'*right}"
        for i in self.ledger:
            descr = i['description']
            amount = f"{i['amount']:.2f}"
            padding = 30 - len(descr[:23]) - len(str(amount))
            template += f"\n{descr[:23]}{' '*padding}{amount}"
        return f"{template}\nTotal: {self.get_balance()}"



def create_spend_chart(categories):
    pass


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)