cinema = input("Enter your old age: ")
cinema = int(cinema)
status = True
while status:
    if cinema <= 3:
        print("You can use FREE!")
    elif cinema > 3 and cinema <= 12:
        print("Buy tickets for $10.")
    elif cinema > 12:
        print("Buy tickets for $15.")
    status = False
