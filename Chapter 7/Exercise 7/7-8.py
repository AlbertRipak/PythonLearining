sandwich_orders = ['tuna', 'kentuki', 'bigmak', 'apple']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich!")
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)
for f in finished_sandwiches:
    print(f.title(), end = ', ')