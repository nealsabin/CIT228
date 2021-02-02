#Exercise 6-2
favNumber = {
    "george":55,
    "elmer":44,
    "joe":14,
    "kim":12,
    "josie":11,
}
print("-----Exercise 6-2-----\n")
for item in favNumber: 
    print(f"{item.title()} your favorite number is {favNumber[item]}")