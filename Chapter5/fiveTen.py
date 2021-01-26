print("------------ Exercise 5-10 ------------")

currentUsers = ["admin","Nsabin","jbrown","Arodgers","HAaron"]
lowerUsers = []
for user in currentUsers:
    lowerUsers.append(user.lower())

newUsers = ["rjohnson","jverlander","nryan","arodgers","haaron"]
lowerNewUsers = []
for new in newUsers:
    lowerNewUsers.append(new.lower())

for newUser in lowerNewUsers:
    if newUser in lowerUsers:
        print(f"{newUser} is NOT available.")
    else:
        print(f"{newUser} is available.")
