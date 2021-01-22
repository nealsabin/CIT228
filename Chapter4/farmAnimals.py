print("-----Ch4 Hands on 3-----\n")

animalList = ["cow","emu","lamb","chicken","goose","goat"]

newList = animalList[:]
newList.append("dog")
newList.append("deer")
newList.append("lion")
newList.append("elk")

print("------Original List-----")
for item in animalList:
    print(item)
print("\n")

print("-----New List------")
for item in newList:
    print(item)
print("\n")

#Exercise 4-10
print(f"The first three items in the new list are: {newList[0:3]}")
print(f"The middle three items in the new list are: {newList[3:6]}")
print(f"The last three items in the new list are: {newList[7:]}")