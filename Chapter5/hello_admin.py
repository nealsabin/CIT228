usernames = ["admin","nsabin","jbrown","arodgers","haaron"]

print("------------Exercise 5-8------------")
for name in usernames:
    if name == "admin":
        print("Hello, admin. Would you like to change any settings?")
    else:
        print(f"Hello, {name}. Hope you're well.")

print("------------Exercise 5-9------------")
usernames = []

if usernames: 
    for name in usernames:
        if name == "admin":
            print("Hello, admin. Would you like to change any settings?")
        else:
            print(f"Hello, {name}. Hope you're well.")
else: 
    print("The list is empty!")