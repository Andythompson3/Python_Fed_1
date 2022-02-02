list = []
for number in range(1,10):
    if number == 1:
        number = (f'1st')
    elif number == 2:
        number = (f'2nd')
    elif number == 3:
        number = (f'3rd')
    else:
        number = (f'{number}th')
    list.append(number)
print(list)
