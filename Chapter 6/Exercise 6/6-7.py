glossary1 = {
    'first': 'georgy',
    'last': 'leps',
    'age': 50,
}
glossary2 = {
    'first': 'albert',
    'last': 'einstein',
    'age': 150,
}
glossary3 = {
    'first': 'ludvig',
    'last': 'clein',
    'age': 480
}

people = [glossary1, glossary2, glossary3]

for person in people:
    for man, man_info in person.items():
        print("It's " + man + ": " + str(man_info))