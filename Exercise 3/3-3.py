auto = ['ford', 'toyota', 'bmw', 'opel']
for car in auto:
    if car in "bmw":
        message = "It's not bed car " + car.upper() + "!"
    else:
        message = "It's not bed car " + car.title() + "!"
    print(message)