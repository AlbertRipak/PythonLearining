sandwich_orders = ['tuna', 'pastrami', 'kentuki', 'pastrami', 'apple', 'pastrami']
finished_sandwiches = []
while sandwich_orders:
    if 'pastrami' in sandwich_orders:
        print("I haven't pastrami!")
        sandwich_orders.remove('pastrami')
    else:
        sandwich = sandwich_orders.pop()
        print("I made your " + sandwich + "!")
        finished_sandwiches.append(sandwich)
print(finished_sandwiches)
for f in finished_sandwiches:
    print(f.title(), end=' ')