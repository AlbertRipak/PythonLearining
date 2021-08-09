rivers = {
    'nile': 'egypt',
    'amazonka': 'avstralia',
    'dnipro': 'urkaine',
}
for key, value in rivers.items():
    print("The " + key.title() + "runs through " + value.title() + ".")

for name in rivers.keys():
    print("The river " + name.title())

for country in rivers.values():
    print("The country " + country.title())