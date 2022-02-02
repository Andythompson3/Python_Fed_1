username = ['Admin', 'John', 'Carl', 'Robin', 'Jessica']
#print(username)
if username:
    for user in username:
        if user == 'Admin':
            print(f'Greetings {user}\nWould you like a full report?')
        else:
            print(f'Greetings {user}')
else:
    print('We need to find more users!')
print('Finish')
