already_taken = {'Matt', 'Smith', 'Rob', 'Barney', 'Marshall', 'Lily'}

take_test = input('Would you like to take our poll? ').capitalize()

if take_test == 'Yes':
    name = input('What is your name? ')
    name = name.capitalize()
    if name in already_taken:
        print('Sorry you already took the test')
    else:
#<<<<<<< HEAD
        already_taken.add(name)
        print('Please follow this link')
else:
    print('Then leave me alone')
print(already_taken)
#=======
# this is called an f string and is a handy way of putting code in your strings
       # print(f'Sounds great {name} here is the test.')
       # already_taken.add(name)
#else:
    #print('Then leave me alone')

#>>>>>>> b889f45120164de0ca53ad53a725ec835ee36bd1
