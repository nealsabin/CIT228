#Hands on #2
#Exercise 10-3
"""print("-----Exercise 10-3 & 10-4-----")

name = input("What is your name? (q to quit)")
with open("Chapter10/names.txt","a") as nameFile:
    while name != 'q':
        name+="\n"
        print(f"Hello, {name}")
        nameFile.write(name)
        name = input("What is your name? (q to quit)")"""

import random
import os
filename="Chapter10/names.txt"
if os.path.exists(filename):
    os.remove(filename)
roomNumbers=[]
with open(filename,"w") as roomFile:
    guest=input("Please enter your name (q to quit): ")
    while guest != 'q':
        number=random.randint(1,50)
        while number in roomNumbers:
            number=random.randint(1,50)
        print(f"{guest} your room number is {number}")
        roomNumbers.append(number)
        guest+=", room# " + str(number) + "\n"
        roomFile.write(guest)
        guest=input("Please enter your name (q to quit): ")

with open(filename) as roomFile:
    print("----------Guest & Room Assignment----------")
    for line in roomFile:
        print(line)