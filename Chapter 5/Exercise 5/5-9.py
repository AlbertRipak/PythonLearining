users = ['admin', 'rad', 'user', 'guest', 'root']
for u in users:
    if len(users) != 0:
        del users[:]
if users:
    print("a")
else:
    print("We need to find some users!")