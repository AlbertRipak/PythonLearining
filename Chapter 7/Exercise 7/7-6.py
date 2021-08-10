'''
#Завершения цикла по проверке условия в команде while:

c = input("Please, enter number < 100: ")
c = int(c)
while c < 100:
    print(c)
    c += 1
'''

#Управление продолжительностью выполнения цикла в
# зависимости от переменной active:
'''
prompt = "Enter message: "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
'''

#Выход из цикла по команде break, если пользователь вводит значение "quit"
sms = "Are you can enter message?: "
while True:
    c = input(sms)
    if c == 'quit':
        break
    else:
        print("\n\t" + c.upper())

    print("\n(If you want stop, enter 'quit'!)")
