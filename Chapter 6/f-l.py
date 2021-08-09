favorite_languages = {
    'jen': [],
    'sarah': ['c', 'python', 'java'],
    'edward': ['ruby'],
    'phil': ['python', 'js'],
}

for key, value in favorite_languages.items():
    if 0 < len(value):
        print(key.title() + "'s favorite languages are: ")
        for v in value:
            if v == 'js':
                print("\t" + v.upper())
            else:
                print("\t" + v.title())
    else:
        print(key.title() + ", please enter your favorite languages!")
#for name, language in favorite_languages.items():
#    print("\nName : " + name.title() + "\nLanguage : " + language.title())

#for key in favorite_languages.keys():
#    print(key.title())
'''
friends = ['jen', 'phil']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(favorite_languages[name] + "\n" )
'''
'''print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() + ".")'''
'''
for name in favorite_languages.keys():
    if 'erin' not in favorite_languages:
        print('not')'''

'''for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")'''
'''
for language in set(favorite_languages.values()):
    print(language.title())'''