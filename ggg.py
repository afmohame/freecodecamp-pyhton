"""#dictionary/set test
pizza = {
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

print(my_set)

food = [{
    'name': 'Margherita Pizza',
    'price': 8.9,
}, {'name': 'chicken wings',
    'price': 2.3,
}, {'name': 'snails',
    'price': 12.7,},
    {'name': 'burger',
    'price': 9.5,}]
for i in food:
    for key, value in i.items():
        print(f"key: {key} price: {value}")

for i in food:
    print(f"key: {i['name']} price: {i['price']}")

#tuples and updating tuples test
import random
tuple1 = (3, 5)
tuple2 = (4, 7)

#select a tuple
print(f"this is second value of tuple1: {tuple1[1]}\nthis is first value of tuple2: {tuple2[0]}") 

tuple3 = (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])

print(f"this is tuple3 which is the sum of tuple1 and tuple2: {tuple3}")

tuple4 = (3, 6, 54, 2, 7 ,0, 98, 23, 15, 4, 11 , 13, 9, 1, 14)
tuple3 = (random.choice(tuple4) + tuple1[0],random.choice(tuple4) + tuple1[1])

print(f"this si the sum of random set of tuple4 and tuple1: {tuple3}")

tuple5 = [(1, 2), (5, 7), (12, 4), (3, 9), (14, 6), (2, 8)]
tuple3 = ((random.choice(tuple5)[0] + tuple1[0],random.choice(tuple5)[1] + tuple1[1]))"""

x = 10
y = 5
picture = ''
"""for i in range(x):
    template = ''
    print(f"x:{i+1}")
    for j in range(y):
        if j+1 == y:
            template += f"{str(j+1)}"
            break
        template += f"{str(j+1)}, "
    print(template)"""
for i in range(x):
    for j in range(y):
        picture += '*'
    picture += f'\n'

print(picture)