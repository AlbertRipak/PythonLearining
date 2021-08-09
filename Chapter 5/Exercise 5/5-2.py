car = 'bmw'
print(car == 'bmw')
print(car != 'bmw')

car = 'Audi'
print(car.lower() == 'audi')
print(car.lower() == 'Audi')

n = 5
print(n > 5)
print(n < 5)
print(n >= 5)
print(n <= 5)
print(n <= 5 and n > 5)
print(n < 5 or n == 5)

l = ['one', 'two', 'three']
for i in l:
    if i == 'two':
        print("i == 'two'")
    else:
        print("i != 'two'")

l2 = ['four', 'five',  'sex']
for v in l2:
    if 'seven' not in v:
        print("Not")
    else:
        print("Yes")