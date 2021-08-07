guest = ['Tom', 'Richard', 'Lia']
print(guest)
p = guest.index('Richard')
print("Hi " + guest[p] + " don't coming!")
p = guest.index('Richard')
guest[p] = 'Dia'
for goues in guest:
    print("Hi " + goues + "!")
print(guest)