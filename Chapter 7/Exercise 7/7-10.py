holiday = {}
active = True
while active:
    name = input("Enter your name: ")
    holid = input("Enter your like place: ")
    repeat = input("You want repeat? (yes/no)")
    holiday[name] = holid
    if repeat == 'no':
        active = False
print(holiday)