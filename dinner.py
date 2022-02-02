friends = ['The rock', 'Ann', 'Stevo']
#print(friends)
for friend in friends:
    person = friend
    print(f"Hello {person} I would like to invite you to my party")
print(f'It looks like {friends[1]} will not be able to join us because she is dead')
del friends[1]
#print(friends)
count = len(friends)
print(f"I am inviting", count, "people to my party")
new_friend = input("What is your name?")
new_friend = new_friend.strip()
friends.insert(1,new_friend)
#print(friends)
for friend in friends:
    person = friend
    print(f"Hello {person} I would like to invite you to my party")
print('By a stroke of of luck I have found a larger table and will be able to invite more people')
friends.insert(0,'rocky')
#print(friends)
friends.insert(2, 'Washington')
print(friends)
friends.append('Elon')
#print(friends)
count = len(friends)
print(f"I am inviting", count, "people to my party")
for friend in friends:
    person = friend
    print(f"Hello {person} I would like to invite you to my party")
print("Sorry I have decided that I don't like more of you so I will only invite two of you")
uninvited = friends.pop(0)
print(f'Sorry {uninvited} I dont need you anymore')
#print(friends)
uninvited = friends.pop(3)
print(f'Sorry {uninvited} I dont need you anymore')
#print(friends)
uninvited = friends.pop(2)
print(f'Sorry {uninvited} I dont need you anymore')
#print(friends)
uninvited = friends.pop(2)
print(f'Sorry {uninvited} I dont need you anymore')
for final_friend in friends:
    best_friend = final_friend
    print(f'I will see you {best_friend} at dinner tonight')
count = len(friends)
print(f"I am inviting", count, "people to my party")
