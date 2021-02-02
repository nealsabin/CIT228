#Exercise 6-5
rivers = {
    'yangtze':'china',
    'volga':'russia',
    'mississippi':'united states',
}
print("-----Exercise 6-5-----\n")

print("Rivers and Countries")
print("--------------------")
for key, value in rivers.items():
    print(f'The {key.title()} river is in {value.title()}')

print("\nRivers")
print("------")
for item in rivers.keys():
    print(item.title())

print("\nCountries")
print("---------")
for item in rivers.values():
    print(item.title())
