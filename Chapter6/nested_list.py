#Hands on 3 - #2
stateMichigan = {
    'capital':'lansing',
    'otherCities': ['Grand Rapids','Detroit','Ann Arbor'],
}

print(f"The capital of Michigan is {stateMichigan['capital'].title()}. Some other cities are: ")
for city in stateMichigan['otherCities']:
    print('\t',city)