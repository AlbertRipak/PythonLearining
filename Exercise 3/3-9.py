language = ['ua', 'en', 'bl', 'jp', 'ru']
language.append('tr')
language.insert(1, 'ge')
a = language.index('en')
print(a)
print(language)
del language[-1]
print(language)
b = language.pop(3)
print("Minus " + b)
print(language)
language[-1] = 'blr'
print(language)
language.remove('blr')
print(language)
print(sorted(language))
print(sorted(language, reverse=True))
language.reverse()
print(language)
language.reverse()
print(language)
language.sort()
print(language)
language.sort(reverse=True)
print(language)
while 0 < len(language):
    del language[0]
    continue
a = len(language)
print(a)
print(language)