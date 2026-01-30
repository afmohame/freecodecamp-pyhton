"""pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}
pizza["name"] = "pute"
for key, value in pizza.items():
    print(f"key: {key} \nvalue: {value}\n")
print(pizza.keys())
print(pizza.items())
print(pizza.values())

my_set = {1, 2, 3, 4, 5, 6}
my_set.add(5)

print(my_set)"""

food = [{
    'name': 'Margherita Pizza',
    'price': 8.9,
}, {'name': 'chicken wings',
    'price': 2.3,
}, {'name': 'snails',
    'price': 12.7,},
    {'name': 'burger',
    'price': 9.5,}]
"""for i in food:
    for key, value in i.items():
        print(f"key: {key} price: {value}")"""

for i in food:
    print(f"key: {i['name']} price: {i['price']}")



