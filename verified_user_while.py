unverified_user= ["Jake", "Steven", "Mark", "Kate"]
verified_user = []
banned_group = []

y = 0
x = len(unverified_user)
while y < x:
    user = unverified_user[0]
    in_question = input(f"Is {user} verified? ").capitalize()
    if in_question == "Yes":
        verified_user.append(unverified_user.pop(0))
    else:
        ban = input(f"Should we ban {user}? ").capitalize()
        if ban == "Yes":
            banned_group.append(unverified_user.pop(0))
        else:
            print("Then he is verified")
            verified_user.append(unverified_user.pop(0))
    y = y + 1
    print(f"Unverified = {unverified_user}")
    print(f"Verified = {verified_user}")
    print(f"Banned = {banned_group}")

print(f"Unverified = {unverified_user}")
print(f"Verified = {verified_user}")
print(f"Banned = {banned_group}")