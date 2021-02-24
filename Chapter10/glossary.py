import json

glossary = {
    "Boolean Expression":"A condition that tests true or false.",
    "Elif":"Statements that are used if you want to test if a condition is true and a different conditino if false.",
    "Tuples":"Similar to a list, but you cannot change the data.",
    "For Loops":"Used to repeat commands for items in a sequence as a list, tuple, dictionary, set or string.",
    "While Loops":"Used to execute commands while a condition tests true.",
}

def menu():
    selection = int(input("\n1-create file, 2-read file, 3-add to file, 4-quit  \n"))
    while selection!=1 and selection!=2 and selection!=3 and selection!=4:
        print("You made an invalid selection, please try again")
        selection = int(input("1-create file, 2-read file, 3-add to file, 4-quit  "))
    return selection

#Write glossary to JSON file
def create(glossary):
    with open("Chapter10/glossaryJSON.json","w") as write_file:
        json.dump(glossary,write_file,indent=4,sort_keys=True)
    print("Done writing JSON data into file.\n")

#Read from glossary JSON file
def read():
    try:         
        filename = "Chapter10/glossaryJSON.json"
        with open(filename) as read_file:
            glossary_loaded = json.load(read_file)
    except FileNotFoundError:
        print("The file doesn't exist")
    else:
        print("\n")
        for key, value in glossary_loaded.items():
            print(f"{key} = {value}")

print("\n")

#Append items to the glossary JSON file
def append(new_item):
    filename = "Chapter10/glossaryJSON.json"
    with open(filename,"r+") as add_file:
        glossary_append=json.load(add_file)
        glossary_append.update(new_item)
        add_file.seek(0)
        json.dump(glossary_append, add_file,indent=4,sort_keys=True)
        print("Data has been added to ", filename)

#Get new key
def get_key():
    new_key=input("Key to add: ")
    return new_key

#Get new value
def get_value():
    new_value=input("Associated value with key: ")
    return new_value

choice=menu()
while choice != 4:
    if choice == 1:
        create(glossary)
    elif choice == 2:
        read()
    elif choice == 3:
        new_key=get_key()
        new_value=get_value()
        new_dictionary_entry={new_key:new_value}
        append(new_dictionary_entry)
    else:
        print("The option you selected is not available, please try again")        
    choice=menu()





