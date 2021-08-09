guest = ['One', 'Two', 'Three', 'Two', 'Five']
print(guest)
b = 'Two'
while b in guest:
    guest.remove('Two')
    continue
print(guest)
