current_users = ['Admin', 'rad', 'user', 'guest', 'Root']
current_users = [e.lower() for e in current_users]
print(current_users)
new_users = ['ron', 'user', 'bob', 'Admin', 'root', 'tomas']
for n in new_users:
    if n.lower() in current_users:
        print("Please " + n.title() + ", change new login.")
    else:
        print("Success!")
        current_users.append(n)

print(current_users, len(current_users))