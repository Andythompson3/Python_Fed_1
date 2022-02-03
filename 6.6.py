already_taken = {'Matt', 'Smith', 'Rob', 'Barney', 'Marshall', 'Lily'}
already_taken = {already_taken.lower() for already_taken in already_taken}
take_test = input('Would you like to take our poll?')
take_test = take_test.lower()
if take_test == 'yes':
    name = input('What is your name?')
    name = name.lower()
    if name in already_taken:
        print('Sorry you already took the test')
    else:
        already_taken.add(name)
        print('Please follow this link')
else:
    print('Then leave me alone')
print(already_taken)
