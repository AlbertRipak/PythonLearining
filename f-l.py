favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

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

for language in set(favorite_languages.values()):
    print(language.title())