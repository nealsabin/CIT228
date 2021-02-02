glossary = {
    "Boolean Expression":"A condition that tests true or false.",
    "Elif":"Statements that are used if you want to test if a condition is true and a different conditino if false.",
    "Tuples":"Similar to a list, but you cannot change the data.",
    "For Loops":"Used to repeat commands for items in a sequence as a list, tuple, dictionary, set or string.",
    "While Loops":"Used to execute commands while a condition tests true.",
}
print("-----Exercise 6-3-----\n")
for item in glossary:
    print(f'{item}:\n\t{glossary[item]}')

#Exercise 6-4
print("\n-----Exercise 6-4-----\n")
glossary["Range() Function"]="Designed to generate a range of numbers."
glossary["Slicing"]="Allows you to select a range within the list."
glossary["Copying"]="You can use the slice operator(:) to copy."
glossary["in"]="keyword used to test if a value is in a list."
glossary["Dictionary"]="Used to store data in key: value pairs."

for key, value in glossary.items():
    print(f'{key}:\n\t{value}')
