respons = {}

polling_active = True

while polling_active:
    name = input("\nWhat is you name?")
    response = input("Whic mountain would you like to climb someday? ")

    response[name] = response