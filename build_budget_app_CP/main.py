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
        return round(sum(i["amount"] for i in self.ledger), 2)
    
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
    bar_chart = "Percentage spent by category"
    category_names = list(n.name for n in categories) #the names of the categories
    max_len = max(len(l) for l in category_names)
    spending_by_cate = {}
    for i in categories:
        spent = -(sum(n["amount"] for n in i.ledger if n['amount'] < 0)) #this sums up the withdrawals from one category at a time
        spending_by_cate[i.name] = spent # this adds the category name and the spent value in the category 
    spending_by_cate["Total"] = sum(spending_by_cate.values()) #total spending for all categories
    percent_spend_per_cate = list(int((100*spending_by_cate[n]/spending_by_cate["Total"])/10)*10 for n in list(spending_by_cate)[:-1])
    #This will fetch the spending per category and divide it by the total spending to have a percentage of total spending per category
    percent = 100
    y_axis = 4
    while percent >= 0:
        space_y = f"{' '*(y_axis - len(str(percent)+'|'))}"
        bar_chart += f"\n{space_y}{percent}|"
        for i in percent_spend_per_cate:
            if i >= percent:
                bar_chart += ' o '
            else:
                bar_chart += '   '
        if percent == 0:
            bar_chart += f"\n{' '*(y_axis)}{'-'*(3*len(categories)+1)}\n{' '*5}"
            for i in range(max_len):
                for letter in category_names:
                    if i < len(letter):
                        bar_chart += f"{letter[i]}  "
                    else:
                        bar_chart += ' '*3 #times 3 because there are 3 spaces 
                if i != max_len - 1:
                    bar_chart += f"\n{' '*5}"
        percent -= 10
    return bar_chart

food = Category('Food')
food.deposit(900, 'deposit')
food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
clothing = Category('Clothing')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
food.transfer(50, clothing)
clothing.withdraw(13.23, "socks")
car = Category("Car")
car.deposit(500, 'deposit')
car.withdraw(236.45, 'new windshield')
clothing.withdraw(19.78, 'pants')

#print(f"{car}\n{food}\n{clothing}")
print(create_spend_chart([food, car, clothing]))