#Exercise 5-1 and 5-2
weather = 'sunny'
print("Is 'weather' == sunny? I predict true.")
print(weather == 'sunny')

print("Is 'weather' == SUnny? I predict true.")
print(weather == 'SUnny'.lower())

print("Is 'weather' == cloudy? I predict false.")
print( weather == 'cloudy')

print("Is 'weather' != sunny? I predecit false.")
print(weather != 'sunny')

number = 10
print("Is 'number' == 10? I predict true.")
print(number == 10)

print("Is 'number' != 10? I predict false.")
print(number != 10)

print("Is 'number' <= 40? I predict true.")
print(number <= 40)

print("Is 'number' >= 10? I predict true.")
print(number >= 10)

print("Is 'number' > 11? I predict false.")
print(number > 11)

print("Is 'number' < 8? I predict false.")
print(number < 8)

stateList = ["Michigan", "Montana", "Utah", "Washington"]
print("Is 'Michigan' in stateList? I predict true.")
print("Michigan" in stateList)

print("Is 'Alaska' in stateList? I predict false.")
print("Alaska" in stateList)

print("Is 'Montana' not in stateList? I predict false.")
print("Montana" not in stateList)

print("Is 'Vermot' in stateList? I predict false.")
print("Vermont" in stateList)

print("Is Michigan and Utah in stateList? I predict true.")
print("Michigan" and "Utah" in stateList)

print("Is Iowa of Florida in stateList? I predict false.")
if "Iowa" in stateList or "Florida" in stateList:
    print("True")
else:
    print("False")
