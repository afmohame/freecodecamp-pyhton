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
        template = ""
        symbols_number = (self.max_chars - len(self.name))
        insert_title = symbols_number//2 # // will throw the decimal away 
        while symbols_number > 0:
            if symbols_number == insert_title:
                template += self.name
            template += self.symbol
            symbols_number -= 1
        for i in self.ledger:
            descr = i['description']
            amount = f"{i['amount']:.2f}"
            length_dict = len(str(amount)) + len(descr)
            space_between = self.max_chars - length_dict
            if length_dict > self.max_chars:
                splice_descr = length_dict - self.max_chars + 1
                #added the +1 so it matches the example
                descr = descr[:-splice_descr]
                length_dict = len(str(amount)) + len(descr)
                space_between = self.max_chars - length_dict
            template += f"\n{descr}{' '*space_between}{amount}"
        return f"{template}\nTotal: {self.get_balance()}"

def create_spend_chart(categories):
    spent = -round(sum(i['amount'] for i in categories.ledger[1:]), -1)
    print(spent)
    template = 'Percentage spent by category'
    symbol = 'o'
    percent = 100
    y_axis = 4
    while percent >= 0:
        space_y = y_axis - len(str(percent)+'|')
        template += f"\n{' '*space_y}{percent}|"
        percent -=10
        if percent == -10:
            template += f"\n{' '*y_axis}-----------------------"
    y_axis = 5
    x_values = len(categories.ledger[1:])
    print(f"x_values: {x_values}")
    return template


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
#print(food)
print(create_spend_chart(food))
