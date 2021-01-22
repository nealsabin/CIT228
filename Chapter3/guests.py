print("------Exercise 3-4------")
guests = ["Grandpa Fred","Grandpa John","Theodore Roosevelt"]
print(guests[0], ", can you make it to dinner on Friday?")
print(guests[1], ", can you make it to dinner on Friday?")
print(guests[2], ", can you make it to dinner on Friday?")

print("------Exercise 3-5------")
print(guests[2],", can not make the dinner Friday")
del guests[2]
guests.insert(2,"James Cook")
print(guests[0], ", can you make it to dinner on Friday?")
print(guests[1], ", can you make it to dinner on Friday?")
print(guests[2], ", can you make it to dinner on Friday?")

print("------Exercise 3-6------")
print("A larger table appeared out of no where. Yay!")
guests = ["Grandpa Fred","Grandpa John","Theodore Roosevelt"]
guests.insert(0,"Honest Abe")
guests.insert(2,"George Washington")
guests.append("Alexander Hamilton")

print(guests[0], ", can you make it to dinner on Friday?")
print(guests[1], ", can you make it to dinner on Friday?")
print(guests[2], ", can you make it to dinner on Friday?")
print(guests[3], ", can you make it to dinner on Friday?")
print(guests[4], ", can you make it to dinner on Friday?")
print(guests[5], ", can you make it to dinner on Friday?")

print("------Exercise 3-7------")
print("What do you know, the larger table has disappeared. I can only invite two people to dinner.")
guests = ["Grandpa Fred","Grandpa John","Theodore Roosevelt"]
guests.insert(0,"Honest Abe")
guests.insert(2,"George Washington")
guests.append("Alexander Hamilton")

removedHam = guests.pop()
removedTeddy = guests.pop()
removedJohn = guests.pop()
removedWash = guests.pop()

print(removedHam, ", my apologies, I can no longer have you for dinner.")
print(removedTeddy, ", my apologies, I can no longer have you for dinner.")
print(removedJohn, ", my apologies, I can no longer have you for dinner.")
print(removedWash, ", my apologies, I can no longer have you for dinner.")

print(guests[0], ", can you make it to dinner on Friday?")
print(guests[1], ", can you make it to dinner on Friday?")

del guests[1]
del guests[0]
print("Here is my final list: ", guests)

print("------Exercise 3-9------")
print("A larger table appeared out of no where. Yay!")
guests = ["Grandpa Fred","Grandpa John","Theodore Roosevelt"]
guests.insert(0,"Honest Abe")
guests.insert(2,"George Washington")
guests.append("Alexander Hamilton")
print("I am expecting ",len(guests), "guests")

print(guests[0], ", can you make it to dinner on Friday?")
print(guests[1], ", can you make it to dinner on Friday?")
print(guests[2], ", can you make it to dinner on Friday?")
print(guests[3], ", can you make it to dinner on Friday?")
print(guests[4], ", can you make it to dinner on Friday?")
print(guests[5], ", can you make it to dinner on Friday?")
