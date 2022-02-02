current_users = ['Admin', 'John', 'Carl', 'Robin', 'Jessica']
current_users = [current_users.lower() for current_users in current_users]
new_users = ['Barney', 'JOHN', 'Matt', 'Ted', 'Jessica']
new_users = [new_users.lower() for new_users in new_users]
for user in new_users:
    if user not in current_users:
        current_users.append(user)
    else:
        print(f'Sorry {user} is already taken')
print (current_users)
