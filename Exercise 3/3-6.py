guest = ['Tom', 'Richard', 'Lia']
print(guest)
guest.insert(0, 'Dia')
guest.insert(2, 'Lex')
guest.append('Gery')
for g in guest:
    print("Hi " + g + "!")
print(guest)