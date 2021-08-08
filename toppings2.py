requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + "!")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


'''requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of " + requested_topping +" right now.")
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")'''