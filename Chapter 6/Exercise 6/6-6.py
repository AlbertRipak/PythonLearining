fl = ['jen', 'phil', 'arnold', 'gery']
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for n in fl:
    if n in favorite_languages.keys():
        print("Thank for you! " + n.title())
    elif n not in favorite_languages.keys():
        print("Change favorite language! " + n.title())
    else:
        print("The end!")