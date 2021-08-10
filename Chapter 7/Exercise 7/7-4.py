pizza = {
    'crust': 'thick',
    'toppings': [],
}
prompt = "\nPlease enter addintions to pizza: "
status = True
while status:
    message = input(prompt)
    if message != 'quit':
        pizza['toppings'].append(message)
        for p in pizza['toppings']:
            print("\nYour pizza have it's tooppings: " + str(p) + "!")
            print("\nIf you want the end enter 'quit'!")
    else:
        print("\nThank you! You change pizza from :")
        for p in pizza['toppings']:
            print("\t" +str(p))
        break