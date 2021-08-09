pizza = ['paperoni', 'meet', 'cheder']
friend_pizzas = pizza[:]
print(pizza)
print(friend_pizzas)

pizza.append('potato')
friend_pizzas.append('carrot')

print("\n")

print("My favorite pizzas are:")
for p in pizza:
    print(p)

print("\nMy friend's favorite pizzas are:")
for f in friend_pizzas:
    print(f)