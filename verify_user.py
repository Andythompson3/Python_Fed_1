unverified_user= ["Jake", "Steven", "Mark", "Kate"]
verified_user = []
banned_group = []

while unverified_user:
    for user in unverified_user:
        user = user.capitalize()
        x = unverified_user.index(user)
        verified_answer = input(f"Is {user} verified? ").capitalize()
        if verified_answer == "Yes":
            verified_user.append(unverified_user.pop(x))
        else:
            ban = input(f"Should we ban {user}?").capitalize()
            if ban == "Yes":
                print(f"Sorry {user} you are no longer welcome")
                banned_group.append(unverified_user.pop(x))
            else:
                print("Then they are verified")
                verified_user.append(unverified_user.pop(x))
        print(f"Unverified = {unverified_user}"
        print(f"Verified = {verified_user}")
        print(f"Banned = {banned_group}")
print("Done")


