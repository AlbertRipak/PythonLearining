guest = ['Dia', 'Tom', 'Lex', 'Richard', 'Lia', 'Gery']
print(guest)

while 2 < len(guest):
    b = guest.pop()
    print("Sorry " + b + "!")

for a in guest:
    print("Hi " + a + "!")

while 0 < len(guest):
    del guest[0]

print(guest)
print(len(guest))