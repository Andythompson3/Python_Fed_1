unverified_user= ["Jake", "Steven", "Mark", "Kate"]
verified_user = []
banned_group = []

while unverified_user:
    for user in unverified_user:
        user = user.capitalize()
        verified_answer = input(f"Is {user} verified? ")
        verified_answer = verified_answer.capitalize()
        if verified_answer == "Yes":
            verified_user = unverified_user.pop()
        else:
            ban = input(f"Should we ban {user}?")
            ban = ban.capitalize()
            if ban == "Yes":
                print(f"Sorry {user} you are no longer welcome")
                banned_group = unverified_user.pop()
            else:
                print("Then they are verified")
                verified_user = unverified_user.pop()
        print(f"Unvarified = {unverified_user}")
        print(f"Varified = {verified_user}")
        print(f"Banned = {banned_group}")
print("Done")


